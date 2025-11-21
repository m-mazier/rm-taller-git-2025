# Implementación de Kiosco CLI

## Requisitos
* Python 3

## Desafío 01:

### Ejecución
* `python src/caja.py < input.txt`

### Decisiones de Diseño y Validaciones

* **Estructuras de Datos:** Se usó un diccionario (`productos`) para el inventario, donde la clave es el código del producto. Esto da acceso súper rápido (O(1)). Las ventas/devoluciones se guardan en una lista simple (`movimientos`).
* **Validaciones:**
    * `ALTA`: Valida que el precio no sea negativo y que la descripción no esté vacía.
    * `STOCK`: Valida que el producto exista.
    * `VENDE`: Valida que el producto exista, que la cantidad sea positiva y que haya stock suficiente.
    * `DEVUELVE`: Valida que el producto exista y que la cantidad sea positiva.
* **Formato:** Se usó formato simple con `f-strings` para alinear las columnas del reporte, con anchos fijos.

### Ejemplos de Entrada/Salida

**Entrada (`input.txt`):**

ALTA chicle Chicle_de_menta 1500
STOCK chicle 10
VENDE chicle 3
REPORTE
DEVUELVE chicle 1
REPORTE
VENDE alfajor 1
FIN

**Salida:**

Sistema de caja iniciado. Escriba FIN para salir.

OK: ALTA chicle

OK: STOCK chicle -> +10

OK: VENDE chicle -> 3 x 1.500 = 4.500

REPORTE
CODIGO     DESCRIPCION          PRECIO      STOCK
chicle     Chicle_de_menta       1.500          7

VENTAS:  unidades=3  monto=Gs 4.500
DEVOLS:  unidades=0  monto=Gs 0
NETO:    Gs 4.500

OK: DEVUELVE chicle -> 1 x 1.500 = -1.500

REPORTE
CODIGO     DESCRIPCION          PRECIO      STOCK
chicle     Chicle_de_menta       1.500          8

VENTAS:  unidades=3  monto=Gs 4.500
DEVOLS:  unidades=1  monto=Gs -1.500
NETO:    Gs 3.000

ERROR: Código 'alfajor' no encontrado.

Cerrando sistema.

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

### Ejemplo de Entrada/Salida

### 1. Bloque de Entrada

#### Entrada (`input.txt`):

ALTA chicle Chicle_menta 1500 
ALTA agua500 Agua_mineral_500 3000 
ALTA galleta Galleta_vainilla 2500 
ALTA cafe Cafe_chico 5000 
STOCK chicle 10 
STOCK agua500 30 
STOCK galleta 12 
STOCK cafe 10 
PROMOS 
VENDE chicle 3 
VENDE agua500 5 
VENDE galleta 1 
VENDE cafe 1 
DEVUELVE galleta 1 
REPORTE 
FIN

### 2. Bloque de Salida Esperada

La salida muestra cómo se aplican los descuentos de 3x2 (chicle) y 10% (agua500), y cómo el reporte consolida los totales y el Top 3.

* **Nota:** Los montos de descuento (Ds.) son visibles.
* **Descuentos aplicados:**
    * Chicle (3x2): 1 unidad gratis = 1500 Gs.
    * Agua (5 unidades): 5 * 3000 = 15000. 10% de 15000 = 1500 Gs.
    * Galleta/Café: 0 Gs (No se cumple el combo en una sola venta).

#### Salida Esperada:

OK: ALTA chicle 
OK: ALTA agua500 
OK: ALTA galleta 
OK: ALTA cafe 
OK: STOCK chicle -> 10 
OK: STOCK agua500 -> 30 
OK: STOCK galleta -> 12 
OK: STOCK cafe -> 10

PROMOCIONES ACTIVAS
3x2 en chicle
10% en agua500 desde 5 unidades
Descuento de 1000 Gs en venta conjunta de galleta y cafe 

OK: VENDE 3 x chicle. Total: 3000 (Desc: 1500) 
OK: VENDE 5 x agua500. Total: 13500 (Desc: 1500) 
OK: VENDE 1 x galleta. Total: 2500 (Desc: 0) 
OK: VENDE 1 x cafe. Total: 5000 (Desc: 0) 
OK: DEVUELVE galleta
 
REPORTE 
CODIGO      DESC                PRECIO      STOCK 
chicle      Chicle_menta          1500          7 
agua500     Agua_mineral_500      3000         25 
galleta     Galleta_vainil        2500         12 
cafe        Cafe_chico            5000          9

VENTAS BRUTAS: 27000 
DESCUENTOS: 3000 
DEVOLUCIONES: -2500 
NETO: 21500

TOP 3 VENDIDOS:
agua500: 5 unidades
chicle: 3 unidades
galleta: 1 unidades 