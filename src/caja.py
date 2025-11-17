import sys

def main():
    """
    Función principal que lee de stdin y ejecuta comandos.
    """
    print("Sistema de caja iniciado. Escriba FIN para salir.")

    # Base de datos en memoria
    productos = {}
    movimientos = []

    for linea in sys.stdin:
        linea = linea.trip()

        if not linea:
            continue

        if linea == "FIN":
            print("Cerrando sistema.")
            break

        # Dividir la línea en "comando" y "argumentos"
        partes = linea.split()
        comando = partes[0].upper()
        args = partes[1:]

        # Comandos
        if comando == "ALTA":
            print(f"DEBUG: Comando ALTA con args: {args}")
            # alta(args, productos)

        elif comando == "STOCK":
            print(f"DEBUG: Comando VENDE con args: {args}")
            # stock(args, productos)

        elif comando == "VENDE":
            print(f"DEBUG: Comando VENDE con args: {args}")
            # vende(args, productos, movimientos)

        elif comando == "DEVUELVE":
            print(f"DEBUG: Comando DEVUELVE con args: {args}")
            # devuelve(args, productos, movimientos)
        
        elif comando == "REPORTE":
            print(f"DEBUG: Comando REPORTE")
            # reporte(productos, movimientos)

        else:
            print(f"ERROR: Comando '{comando}' no reconocido.")

        print("")

# Esto hace que main() se ejecute solo cuando corremos el archivo
if __name__ == "__main__":
    main()