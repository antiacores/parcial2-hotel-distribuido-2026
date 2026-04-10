# Declaración de uso de IA

> Llenen este archivo si alguno de los dos usó alguna herramienta de IA generativa (Claude, ChatGPT, Copilot, Gemini, etc.) durante el examen. Hacerlo es **obligatorio** y se evalúa con honestidad: declarar correctamente no penaliza, lo que penaliza es **no declarar** y que se detecte uso.
>
> Indiquen también **quién** de los dos integrantes la usó (puede ser uno solo, ambos, o ninguno).

## ¿Usaron IA?

- [x] Sí
- [ ] No

## ¿Quién la usó?

- [ ] Integrante 1
- [ ] Integrante 2
- [x] Ambos

---

## Si la respuesta es "Sí":

### Herramientas usadas
Claude.ai
ChatGPT-5.3

-

### Prompts principales
Listen los 3-5 prompts más importantes que escribieron y para qué los usaron.

1. **Prompt:** "¿Qué significa auto_ack=True en pika y cuál es el riesgo de usarlo?"
   **Para qué:** Entender conceptualmente el bug B3 antes de arreglarlo.
   **Quién lo usó:** Integrante 1 (Antía)
   **Qué tan útil fue:** 4

2. **Prompt:** "¿Cómo se hace un try/except en un endpoint de FastAPI para devolver un HTTPException con status 503?"
   **Para qué:** Recordar la sintaxis correcta para el manejo de errores en FastAPI (B2).
   **Quién lo usó:** Integrante 1 (Antía)
   **Qué tan útil fue:** 3

3. **Prompt:** "¿Cómo bindear una queue a dos routing keys distintos en pika?"
   **Para qué:** Confirmar que se pueden hacer dos llamadas a queue_bind sobre la misma queue para payment.completed y payment.failed.
   **Quién lo usó:** Integrante 1 (Antía)
   **Qué tan útil fue:** 4

4. **Prompt:** ¿Por qué se procesa dos veces el mismo booking_id si se reintenta el mensaje?
   **Para qué:** Entender el porqué de los cobros duplicados y poder detectar el problema de idempotencia
   **Quién lo usó:** Integrante 2 (Fernando)
   **Qué tan útil fue:** 5

5. **Prompt:** "¿Cómo hago para que RabbitMQ no procesa dos veces el mismo mensaje?"
   **Para qué:** Validar que la solución realmente funciona
   **Quién lo usó:** Integrante 2
   **Qué tan útil fue:** 4

### ¿En qué partes los apoyó?

- Explicación del comportamiento de ´auto_ack´ y cuándo usar ´basic_nack´
- Sintaxis de manejo de excepciones en FastAPI
- Confirmar el patrón de doble binding en pika para el notification-service
- Principalmente en payment-service, porque no entendía completamente cómo hacerlo idempotente ni el problema de RabbitMQ del reprocesamiento de eventos. 

### ¿Hubo cosas en las que la IA dio respuestas incorrectas o que tuvieron que corregir?
(Ser honestos aquí suma puntos de criterio)

- Sugirió usar ´basic_ack´ en el bloque ´except´ del callback, lo cual sería incorrecto porque estaría confirmando un mensaje que no se procesó bien. Se corrigió a ´basic_nack´ con ´requeue=True´.

### ¿Qué decidieron hacer manualmente sin IA y por qué?

- La lectura del código fuente y la identificación de cada bug se hizo manualmente revisando los comentarios ´# BUG:´ directamente en el repo.
- Los commits, ramas y flujo de Git se manejaron manualmente.
- La documentación en ´DECISIONES.md´ se redactó con palabras propias para reflejar el razonamiento real detrás de cada cambio.