def cambio_voraz(monto, denominaciones):
    # 1. Preparación: Ordenar las denominaciones de mayor a menor. 
    #    Esta es la CLAVE de la estrategia voraz.
    denominaciones.sort(reverse=True)
    
    # Inicializar el resultado y el monto restante
    resultado = {}
    monto_restante = monto
    
    # 2. Iteración Voraz
    for moneda in denominaciones:
        # Paso Voraz: Tomar la MAYOR cantidad posible de la moneda actual 
        # sin exceder el monto restante.
        
        # Calcular cuántas monedas de esta denominación caben en el monto restante
        cantidad = monto_restante // moneda
        
        # Si se usa al menos una moneda, registrarla
        if cantidad > 0:
            resultado[moneda] = cantidad
            
            # Actualizar el monto restante
            monto_restante -= cantidad * moneda
        
      
        if monto_restante == 0:
            break
            
    # 3. Verificación
    if monto_restante > 0:
        print(f"Advertencia: No se pudo dar el cambio completo. Faltan: {monto_restante}")
        
    return resultado

# --- Ejemplo de Uso ---
monto_a_pagar = 87 # Ejemplo: 87 centavos/unidades
monedas_disponibles = [1, 5, 10, 25] # Denominaciones típicas (centavos)

cambio = cambio_voraz(monto_a_pagar, monedas_disponibles)

print(f"Monto Total: {monto_a_pagar}")
print("Cambio Óptimo (Voraz):")
total_monedas = 0
for moneda, cantidad in cambio.items():
    print(f"  - {cantidad} moneda(s) de {moneda}")
    total_monedas += cantidad

print(f"\nTotal de Monedas Utilizadas: **{total_monedas}**")