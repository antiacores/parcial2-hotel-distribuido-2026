# Decisiones técnicas

> Documenten brevemente las decisiones que tomaron resolviendo el examen. No copien del enunciado: expliquen con sus palabras qué hicieron y por qué. La intención es que al revisar pueda entender el razonamiento, no que repitan el problema.

---

## Bugs arreglados (Tier 1)

### B1 — Routing key
**Qué encontré:**
El ´booking.api´ usaba el routing key ´booking.create´, pero ´availability-service´ tiene ´booking.requested´.

**Cómo lo arreglé:**
Cambié el routing key de ´booking.create´ a ´booking.requested´.

**Por qué esto era un problema:**
Como el exchange es de tipo TOPIC, RabbitMQ enruta los mensajes según el routing key. Si no tienen el mismo key (el publisher y el consumer), el mensaje no llega al consumer.

---

### B2 — Manejo de error en publish
**Qué encontré:**
La llamada a ´publish_booking´ no había ningún manejo de errores, el cliente recibía un ´202 OK´ aunque el evento nunca se había publicado por algún fallo.

**Cómo lo arreglé:**
Envolví la llamada en un ´try/except´. Para que si hay alguna excepción, devuelva que el servicio no está disponible.

**Por qué esto era un problema:**
El cliente creía que su reserva había sido aceptada cuando en realidad el broker no tenía ningún evento al respecto, dejando que los demás servicios que dependen de ella se enteraran de la reserva.

---

### B3 — Ack manual
**Qué encontré:**
Availability-service utilizaba auto_ack=True, y eso hacía que los mensajes fueran procesados antes de que el callback terminara de ejecutarse.

**Cómo lo arreglé:**
Desactivé auto_ack e hice el manejo manual de ACK usando basic_ack cuando el procesamiento es exitoso y basic_nack en caso de que falle.

**Por qué esto era un problema:**
Porque si el servicio fallaba mientras se procesaba, entonces el mensaje ya era considerado como entregado y por lo tanto, se perdía. Generaba inconsistencias en el sistema. Con ACK manual los mensajes solo se confirman cuando fueron procesados correctamente.

---

### B6 — Credenciales en env vars
**Qué encontré:**
La URL de conexión a Postgres tenía credenciales hardcodeadas en el código, lo cual es un problema de seguridad ya que es información sensible para cualquiera que entre al proyecto.

**Cómo lo arreglé:**
Se eliminó la URL y se reemplazó por variables de entorno mediante os.getenv().

**Por qué esto era un problema:**
Porque se compromete la seguridad del sistema al exponer las credenciales. Con variables de entorno, la configuración se vuelve flexible y segura.

---

## notification-service completado

**Qué TODOs había:**
Declarar el exchange y bindear la queue, implementar el callback de procesamiento, e iniciar el consumer.

**Cómo los implementé:**
- TODO 1: Declaré el exchange ´hotel´ de tipo topic, creé la queue ´notifications´ y la bindeé para ´payment.completed´ y para ´payment.failed´.
- TODO 2: Implementé el callback que parsea el JSON del mensaje, extrae ´booking_id´y ´guest´, convierte el routing_key a mayúsculas para obtener el nombre del evento, y loggea con el formato requerido.
- TODO 3: Inicié el consumer con ´basic_consume´ usando ´auto_ack=False´ para el ack manual, seguido de ´start_consuming´.

**Decisiones de diseño que tomé:**
Usé ´method.routing_key.upper().replace(".", "_")´ para derivar el nombre del evento directamente del routing key.

---

## Bugs arreglados (Tier 2)

### B4 — Overlap de fechas
**Qué encontré:**
El availability-service utilizaba una validación incorrecta para detectar problemas en las reservas, solo comparaba únicamente "check_in == check_in." Esto solo detectaba coincidencias de fechas y no identificaba superposiciones.

**Cómo lo arreglé:**
Reemplacé la condición por una validación correcta de traslape de fechas utilizando la lógica:
´check_in < check_out AND check_out > check_in´
Esto se implementó en la función find_available_room.

**Por qué esto era un problema:**
Porque se podía hacer reservas con fechas superpuestas en la misma habitación, generaba incosistencias. Ahora se dectanta todos los casos de superposición y se evita asignar habitacones ocupadas.

### B5 — Race condition con `with_for_update()`
**Qué encontré:**
Se hacían dos operaciones continuas: primero se consultaba disponibilidad y luego reserva. Antes, se podía que más de un consumer viera la habitación como disponible e insertarlos

**Cómo lo arreglé:**
Se agregó .with_for_update() en la query que valida conflictos dentro de find_available_room, bloqueando las filas relevantes durante la transacción.

**Por qué esto era un problema:**
Permitía que múltiples reservas pudieran confirmarse para la misma habitación y fecha. Con el bloqueo, se garantiza consistencia.

### B7 — Idempotencia
**Qué encontré:**
Payment-service no era idempotente. Si RabbitMQ reentregaba un evento booking.confirmed, el mismo booking_id se procesaba nuevamente, generando cobros duplicados.

**Cómo lo arreglé:**
Se creó una tabla processed_events con event_id como clave primaria.
Antes de procesar el pago, se intenta insertar el booking_id en esta tabla:
Si el insert es exitoso entonces el evento no ha sido procesado y se continúa con el cobro.
Si falla entonces el evento ya fue procesado y se ignora el cobro

**Por qué esto era un problema:**
RabbitMQ trabaja con entrega "al menos una vez", por eso un evento puede ser procesado varias veces. Sin idempotencia, hay muchos peligros como cobros duplicados e inconsistencia. Ahora, se garantiza que booking_id se procese una sola vez.

---

## Bonus que implementé (si aplica)

---

## Cosas que decidí NO hacer

(Ej: "no agregué tests porque preferí enfocarme en el flujo end-to-end", "no implementé saga porque no me dio tiempo", etc.)

---

## Si tuviera más tiempo, lo siguiente que mejoraría sería:
