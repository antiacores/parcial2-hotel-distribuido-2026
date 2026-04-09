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

---

### B6 — Credenciales en env vars

---

## notification-service completado

**Qué TODOs había:**

**Cómo los implementé:**

**Decisiones de diseño que tomé:**

---

## Bugs arreglados (Tier 2)

### B4 — Overlap de fechas

### B5 — Race condition con `with_for_update()`

### B7 — Idempotencia

---

## Bonus que implementé (si aplica)

---

## Cosas que decidí NO hacer

(Ej: "no agregué tests porque preferí enfocarme en el flujo end-to-end", "no implementé saga porque no me dio tiempo", etc.)

---

## Si tuviera más tiempo, lo siguiente que mejoraría sería:
