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

            elif comando == "DEVUELVE":
                # DEVUELVE <codigo> <cantidad>
                codigo = args[0]
                cant = int(args[1])

                if codigo in productos:
                    productos[codigo]["stock"] += cant
                    # Registramos devolución (montos negativos)
                    precio = productos[codigo]["precio"]
                    monto = precio * cant * -1

                    movimientos.append({
                        "tipo": "DEVOLUCION",
                        "codigo": codigo,
                        "cantidad": cant,
                        "bruto": monto,
                        "descuento": 0,
                        "neto": monto
                    })
                    print(f"OK: DEVUELVE {codigo}")

            elif comando == "PROMOS":
                print("PROMOCIONES ACTIVAS")
                
                contador_promo = 1

                for descripcion in promociones_activas:

                    print(f"{contador_promo}) {descripcion}")

                    contador_promo += 1

            elif comando == "REPORTE":
                print("REPORTE")

                # --- 1. Reporte de Inventario (Tabla) ---
                print(f"{'CODIGO':<10} {'DESC':<15} {'PRECIO':>8} {'STOCK':>6}")
                for c, p in productos.items():
                    # slicing para acortar la descripción
                    print(f"{c:<10} {p['desc'][:15]:<15} {p['precio']:>8.0f} {p['stock']:>6}")

                # --- 2. Cálculo de Totales ---
                total_ventas_brutas = 0
                total_descuentos_aplicados = 0
                total_devoluciones_neto = 0

                for movimiento in movimientos:
                    if movimiento['tipo'] == 'VENTA':
                        total_ventas_brutas += movimiento['bruto']
                        total_descuentos_aplicados += movimiento['descuento']

                    elif movimiento['tipo'] == 'DEVOLUCION':
                        total_devoluciones_neto += movimiento['neto']

                # Calculamos el neto final
                total_neto_final = total_ventas_brutas - total_descuentos_aplicados + total_devoluciones_neto

                print(f"\nVENTAS BRUTAS:   {total_ventas_brutas:.0f}")
                print(f"DESCUENTOS:      {total_descuentos_aplicados:.0f}")
                print(f"DEVOLUCIONES:    {total_devoluciones_neto:.0f}")
                print(f"NETO:            {total_neto_final:.0f}")

                # --- 3. TOP 3 ---

                # 1. Contar ventas por producto
                conteo_ventas = {}
                for m in movimientos:
                    if m['tipo'] == 'VENTA':
                        cod = m['codigo']
                        # Usamos get() para iniciar en 0 si el código no existe
                        conteo_ventas[cod] = conteo_ventas.get(cod, 0) + m['cantidad']

                # 2. Convertimos el diccionario a una lista de tuplas para poder ordenar
                lista_para_ordenar = []
                for codigo_vendido, cantidad_vendida in conteo_ventas.items():
                    lista_para_ordenar.append((codigo_vendido, cantidad_vendida))

                # 3. Ordenamos la lista

                ranking = sorted(lista_para_ordenar, key=lambda x: x[1], reverse=True)

                print("\nTOP 3 VENDIDOS:")


                # 4. Imprimimos los primeros 3 resultados del ranking
                for cod, cant in ranking[:3]:
                    print(f"- {cod}: {cant} unidades")

            else:
                pass
        
        except Exception as e:
            print(f"ERROR procesando comando: {e}")

if __name__ == "__main__":
    main()