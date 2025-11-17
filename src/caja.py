import sys

# --- Lógica de Negocio ---

def alta(args, productos_db):
    try:
        # ALTA <codigo> <descripcion...> <precio>
        precio = float(args[-1])
        codigo = args[0]
        descripcion = " ".join(args[1:-1])

        if precio < 0 or not descripcion:
            print("ERROR: Argumentos inválidos para ALTA.")
            return
        
        productos_db[codigo] = {"desc": descripcion, "precio": precio, "stock": 0}
        print(f"OK: ALTA {codigo}")
    except (ValueError, IndexError):
        print("ERROR: Uso: ALTA <codigo> <descripcion...> <precio>")

def stock(args, productos_db):
    try:
        # STOCK <codigo> <cantidad>
        codigo = args[0]
        cantidad = int(args[1])

        if codigo not in productos_db:
            print(f"ERROR: Código '{codigo}' no encontrado.")
            return
        
        productos_db[codigo]["stock"] += cantidad
        print(f"OK: STOCK {codigo} -> {'+' if cantidad > 0 else ''}{cantidad}")
    except (ValueError, IndexError):
        print("ERROR: Uso: STOCK <codigo> <cantidad>")

def vende(args, productos_db, movimientos):
    try:
        # VENDE <codigo> <cantidad>
        codigo = args[0]
        cantidad = int(args[1])

        if cantidad <= 0:
            print("ERROR: La cantidad debe ser positiva.")
            return
        if codigo not in productos_db:
            print(f"ERROR: Código '{codigo}' no encontrado.")
            return
        
        producto = productos_db[codigo]
        if producto["stock"] < cantidad:
            print(f"ERROR: Stock insuficiente para '{codigo}'. (Stock: {producto['stock']})")
            return

        # Actualizar stock
        producto["stock"] -= cantidad
        # Registrar movimiento
        monto = producto["precio"] * cantidad
        movimientos.append({"tipo": "VENTA", "monto": monto, "cantidad": cantidad})
        
        print(f"OK: VENDE {codigo} -> {cantidad} x {producto['precio']} = {monto}")
    except (ValueError, IndexError):
        print("ERROR: Uso: VENDE <codigo> <cantidad>")

def devuelve(args, productos_db, movimientos):
    try:
        # DEVUELVE <codigo> <cantidad>
        codigo = args[0]
        cantidad = int(args[1])

        if cantidad <= 0:
            print("ERROR: La cantidad debe ser positiva.")
            return
        if codigo not in productos_db:
            print(f"ERROR: Código '{codigo}' no encontrado.")
            return

        producto = productos_db[codigo]
        # Actualizar stock
        producto["stock"] += cantidad
        # Registrar movimiento (negativo)
        monto = producto["precio"] * cantidad * -1
        movimientos.append({"tipo": "DEVOLUCION", "monto": monto, "cantidad": cantidad})
        
        print(f"OK: DEVUELVE {codigo} -> {cantidad} x {producto['precio']} = {monto}")
    except (ValueError, IndexError):
        print("ERROR: Uso: DEVUELVE <codigo> <cantidad>")

# --- Función Principal ---

def main():
    """
    Función principal que lee de stdin y ejecuta comandos.
    """
    print("Sistema de caja iniciado. Escriba FIN para salir.")

    # Base de datos en memoria
    productos = {}
    movimientos = []

    for linea in sys.stdin:
        linea = linea.strip()

        if not linea: continue

        if linea == "FIN":
            print("Cerrando sistema.")
            break

        # Dividir la línea en "comando" y "argumentos"
        partes = linea.split()
        comando = partes[0].upper()
        args = partes[1:]

        # Comandos
        if comando == "ALTA":
            alta(args, productos)
        elif comando == "STOCK":
            stock(args, productos)
        elif comando == "VENDE":
            vende(args, productos, movimientos)
        elif comando == "DEVUELVE":
            devuelve(args, productos, movimientos)
        elif comando == "REPORTE":
            print(f"DEBUG: Comando REPORTE")
            # reporte(productos, movimientos)
        else:
            print(f"ERROR: Comando '{comando}' no reconocido.")

        print("")

# Esto hace que main() se ejecute solo cuando corremos el archivo
if __name__ == "__main__":
    main()