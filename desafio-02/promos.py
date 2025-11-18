def calcular_descuento(items_de_venta, productos_db, promociones_activas):
    descuento_total = 0

    cantidad_chicles = 0
    cantidad_agua = 0
    tengo_galleta = False
    tengo_cafe = False

    for item in items_de_venta:
        codigo = item[0]
        cantidad = item[1]

        if codigo == 'chicle':
            cantidad_chicles += cantidad
        elif codigo == 'agua500':
            cantidad_agua += cantidad
        elif codigo == 'galleta':
            tengo_galleta = True
        elif codigo == 'cafe':
            tengo_cafe = True
    
    # --- 3x2 en chicle ---
    # Si hay 3 o más chicles
    if cantidad_chicles >= 3:
        precio_chicle = productos_db['chicle']['precio']

        grupos_de_tres = int(cantidad_chicles / 3)

        monto_a_descontar = grupos_de_tres * precio_chicle
        descuento_total += monto_a_descontar
    
    # --- 10% en agua500 ---
    # Si hay 5 o más aguas
    if cantidad_agua >= 5:
        precio_agua = productos_db['agua500']['precio']

        total_precio_aguas = cantidad_agua * precio_agua

        monto_a_descontar = total_precio_aguas * 0.10
        descuento_total += monto_a_descontar

    # --- Combo Galleta + Café ---
    if tengo_galleta and tengo_cafe:
        descuento_total += 1000

    return descuento_total