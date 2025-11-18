import sys
from promos import calcular_descuento

def main():
    print("Sistema de Caja 2.0 iniciado. Escriba FIN para salir.")

    productos = {}
    movimientos = []

    promociones_activas = [
        "3x2 en chicle",
        "10% en agua500 desde 5 unidades",
        "Descuento de 1000 Gs en venta conjunta de galleta y café"
    ]

    for linea in sys.stdin:
        linea = linea.strip()
        if not linea: continue
        if linea == "FIN":
            break

        partes = linea.split()
        comando = partes[0].upper()
        args = partes[1:]

        try:
            if comando == "ALTA":
                # ALTA <codigo> <descripcion> <precio>
                precio = float(args[-1])
                codigo = args[0]
                desc = " ".join(args[1:-1])
                productos[codigo] = {"desc": desc, "precio": precio, "stock": 0}
                print(f"OK: ALTA {codigo}")

            elif comando == "STOCK":
                # STOCK <codigo> <cantidad>
                codigo = args[0]
                cant = int(args[1])
                if codigo in productos:
                    productos[codigo]["stock"] += cant
                    print(f"OK: STOCK {codigo} -> {productos[codigo]['stock']}")
                else:
                    print("ERROR: Producto no encontrado")

            elif comando == "VENDE":
                # VENDE <codigo> <cantidad>
                codigo = args[0]
                cant = int(args[1])

                if codigo not in productos:
                    print(f"ERROR: {codigo} no existe")
                    continue

                if productos[codigo]['stock'] < cant:
                    print(f"ERROR: Stock insuficiente")
                    continue
                
                items_venta = [(codigo, cant)]

                descuento = calcular_descuento(items_venta, productos, promociones_activas)

                precio_unit = productos[codigo]["precio"]
                bruto = precio_unit * cant
                neto = bruto - descuento

                productos[codigo]["stock"] -= cant

                movimientos.append({
                    "tipo": "VENTA",
                    "codigo": codigo,
                    "cantidad": cant,
                    "bruto": bruto,
                    "descuento": descuento,
                    "neto": neto
                })

                print(f"OK: VENDE {cant} x {codigo}. Total: {neto:.0f} (Desc: {descuento:.0f})")
            else:
                pass
        
        except Exception as e:
            print(f"ERROR procesando comando: {e}")

if __name__ == "__main__":
    main()