# Implementación de Kiosco CLI

## Ejecución
* `python src/caja.py < input.txt`

## Requisitos
* Python 3

## Decisiones de Diseño y Validaciones

* **Estructuras de Datos:** Se usó un diccionario (`productos`) para el inventario, donde la clave es el código del producto. Esto da acceso súper rápido (O(1)). Las ventas/devoluciones se guardan en una lista simple (`movimientos`).
* **Validaciones:**
    * `ALTA`: Valida que el precio no sea negativo y que la descripción no esté vacía.
    * `STOCK`: Valida que el producto exista.
    * `VENDE`: Valida que el producto exista, que la cantidad sea positiva y que haya stock suficiente.
    * `DEVUELVE`: Valida que el producto exista y que la cantidad sea positiva.
* **Formato:** Se usó formato simple con `f-strings` para alinear las columnas del reporte, con anchos fijos.

## Ejemplos de Entrada/Salida

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

OK: ALTA chicle

OK: STOCK chicle -> +10

OK: VENDE chicle -> 3 x 1500.0 = 4500.0

REPORTE 
CODIGO      DESCRIPCION     PRECIO      STOCK 
chicle      Chicle_de_menta 1500        7
VENTAS: unidades=3 monto=Gs 4500 
DEVOLS: unidades=0 monto=Gs 0 
NETO: Gs 4500

OK: DEVUELVE chicle -> 1 x 1500.0 = -1500.0

REPORTE 
CODIGO      DESCRIPCION     PRECIO      STOCK 
chicle      Chicle_de_menta 1500        8
VENTAS: unidades=3 monto=Gs 4500 
DEVOLS: unidades=1 monto=Gs -1500 
NETO: Gs 3000

ERROR: Comando 'VENDE' no reconocido.

Cerrando sistema.