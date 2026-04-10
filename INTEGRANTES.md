# Integrantes de la pareja

> **Llenen este archivo antes de empezar a tocar código**. Es parte de la calificación (4 pts) y la base para evaluar el balance de trabajo entre los dos.

## Integrante 1

- **Antía Cores Barrón:**
- **196841:**
- **antiacores0@gmail.com:**
- **antiacores:**

## Integrante 2

- **Fernando Agustín Hernández Rivas**
- **195468**
- **fernandohdezrivas@gmail.com**
- **fernandoorivas**

---

## División inicial del trabajo

> Antes de empezar, acuerden quién va a tomar qué. Pueden dividir por servicio, por tier, por bug, o como les acomode. Si después cambian, actualicen la tabla.

| Bug / Tarea | Responsable principal | Apoyo |
|---|---|---|
| B1 — routing key en booking-api | Antía | - |
| B2 — manejo de error en publish | Antía | - |
| B3 — auto_ack en availability-service | | - |
| B4 — overlap de fechas | Fernando | - |
| B5 — race condition con `with_for_update()` | Fernando | - |
| B6 — credenciales hardcodeadas | Fernando | - |
| B7 — idempotencia en payment-service | Fernando | - |
| `notification-service` (TODOS) | Antía | - |
| `notification-service` en docker-compose | Antía | - |
| Capturas de RabbitMQ | Antía | - |
| Logs end-to-end | Antía | - |
| `DECISIONES.md` | Fernando | Antía |
| `PROMPTS.md` | Antía | Fernando |
| (otro) | | |

---

## Resumen final del trabajo

> Llenen esto al terminar. Una o dos frases por integrante explicando qué cosas hicieron principalmente. La idea no es competir, es que quede claro que ambos participaron.

### Lo que hizo Integrante 1
- B1: Corregí el routing_key de ´booking.created´ a ´booking.requested´.
- B2: Agregué manejo de errores con un ´try/except´ para devolver 503 si falla el publish a RabbitMQ.
- notification-service: Completé los 3 TODOs (declaración del exchange, implementación del callback con log estructurado y arranque del consumer con ack manual)
- docker-compose: Agregué el servicio de las notificaciones (notification-service).
- Redacción: Redacté DECISIONES.md y PROMPTS.md

### Lo que hizo Integrante 2
- B3: Configuré el ACK manualmente para confirmar mensajes solo después de haber sido procesados correctamente.
- B4: Hice la validación para poder evitar reservas con las mismas fechas en la misma habitación
- B5: Agregué bloqueo a nivel de base de datos en la consulta de disponibilidad, evitando que múltiples procesos reserven la misma habitación simultáneamente.
- B6: La configuración de conexión a la base datos ahora es mediante variables de entorno para mejorar la seguridad.
- B7: Se implementó idempotencia creando una tabla "processed_events" para poder evitar que un mismo evento sea procesado más de una vez y evitar cobros duplicados.


---

## Notas sobre el trabajo en pareja

(Opcional) ¿Hubo algo difícil de coordinar? ¿Mejoras al flujo de trabajo en pareja para la próxima vez?

En general, la coordinación de tareas fue sencilla. Sin embargo, en la rama de teamwork, donde actualizábamos el archivo de decisiones, sí tuvimos mucha comunicación de lo que hacíamos para evitar sobrescribir cambios, eliminar información del otro o generar conflictos en el repositorio. Para mejorar, sería útil definir mejor quién edita cada parte o hacer commits más frecuentes y coordinados.