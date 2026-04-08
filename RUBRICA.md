# Rúbrica de evaluación

**Total: 100 puntos** — Trabajo en parejas (2 personas)

---

## Código — 70 pts

### Tier 1 — Imprescindible (45 pts)

| Criterio | Puntos |
|---|---|
| B1 — routing key correcto en `booking-api` | 5 |
| B2 — manejo de error en publicación, devuelve 503 | 5 |
| B3 — `auto_ack=False` con ack manual en `availability-service` | 5 |
| B6 — credenciales en env vars en `payment-service` | 5 |
| `notification-service` completado (TODOs resueltos) | 12 |
| `notification-service` agregado a `docker-compose.yml` | 5 |
| Flujo end-to-end funciona (`POST /bookings` → notificación) | 8 |

### Tier 2 — Intermedio (20 pts)

| Criterio | Puntos |
|---|---|
| B4 — overlap de fechas correcto | 7 |
| B5 — `with_for_update()` resuelve race condition | 7 |
| B7 — idempotencia en `payment-service` | 6 |

### Tier 3 — Bonus (5 pts)

| Criterio | Puntos |
|---|---|
| Saga compensatoria (release de habitación si pago falla) | 3 |
| Tests, observabilidad o mejoras significativas | 2 |

---

## Commits + Evidencia + Documentación de pareja — 30 pts

| Criterio | Puntos |
|---|---|
| Commits atómicos con mensajes claros (no `fix`, no `wip`) | 8 |
| `evidence/` completo (capturas RabbitMQ, logs, ejemplos curl) | 10 |
| `DECISIONES.md` justificando los cambios | 4 |
| `INTEGRANTES.md` (nombres, matrículas y división de trabajo clara) | 4 |
| `PROMPTS.md` lleno honestamente | 4 |

---

## Penalizaciones

| Falta | Castigo |
|---|---|
| Sin commits (todo aplastado en uno solo) | -10 |
| Sin evidencia | -10 |
| `INTEGRANTES.md` vacío o sin división de trabajo | -8 |
| Todos los commits son de un solo integrante (colaboración no balanceada) | -8 |
| `PROMPTS.md` vacío y se detecta uso de IA | -5 |
| No hace fork (sube ZIP por otro lado) | -10 |
| Copia evidente entre parejas distintas | suspende a ambas |
