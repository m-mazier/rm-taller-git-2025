# Mi Kiosco CLI

## Requisitos
* Python 3

## Desafío 02: Sistema con Módulo de Descuentos

### Ejecución
Correr desde la raíz del proyecto:
`python desafio-02/caja.py`

### Estructura
* `caja.py`: Maneja la interacción con el usuario (CLI) y el inventario.
* `promos.py`: Módulo puro que recibe una lista de items y devuelve el descuento calculado según reglas (3x2, 10%, Combo).

### Supuestos
* El comando `VENDE` procesa un ítem a la vez. Por tanto, el descuento "Combo" (Galleta+Cafe) está implementado en la lógica pero requiere que ambos items se pasen juntos (lo cual requeriría un cambio en el CLI para soportar carritos).
* El reporte "Top 3" cuenta unidades totales vendidas (sin restar devoluciones).