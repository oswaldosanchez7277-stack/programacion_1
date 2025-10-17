
pokedex = []
def agregar_pokemon():
    """Pide nombre, un tipo obligatorio, y un segundo tipo opcional."""
    print("\n Agregar Pokémon")
    nombre = input("Nombre del Pokémon: ").strip()
    tipo1 = input("Tipo principal (ej: Fuego): ").strip()
    tipo2 = input("Segundo tipo (Opcional, deja vacío si no tiene): ").strip() or "N/A"
    nuevo_pokemon = {
        "nombre": nombre,
        "tipo_principal": tipo1,
        "tipo_secundario": tipo2 # Si no escribió nada, será "N/A"
    }
    pokedex.append(nuevo_pokemon)
    print(f"¡{nombre} ha sido agregado al Pokédex!")
def ver_pokemones():
    """Muestra todos los Pokémon en la lista usando un bucle for."""
    print("\n Pokédex Actual:")
    if not pokedex:
        print("El Pokédex está vacío.")
        return
    print("ID: Nombre: Tipo Principal: Tipo Secundario: ")
    for i, p in enumerate(pokedex):
        id_str = str(i + 1)
        nombre_str = p['nombre']
        tipo1_str = p['tipo_principal']
        tipo2_str = p['tipo_secundario']
        print(f"{id_str} | {nombre_str} | {tipo1_str} | {tipo2_str}")
def eliminar_pokemon():
    """Elimina un Pokémon de la lista por su ID (posición + 1)."""
    if not pokedex:
        print("\nEl Pokédex está vacío, no hay nada que eliminar.")
        return
    ver_pokemones() 
    try:
        id_a_eliminar = int(input("\nIntroduce el ID del Pokémon a eliminar (0 para cancelar): "))
        if id_a_eliminar == 0:
            print("Operación cancelada.")
            return
        indice = id_a_eliminar - 1
        if 0 <= indice < len(pokedex):
            pokemon_eliminado = pokedex.pop(indice) 
            print(f"¡{pokemon_eliminado['nombre']} ha sido eliminado!")
        else:
            print(f"Error: ID {id_a_eliminar} no válido.")
    except ValueError:
        print("Error: Debes introducir un número entero.")
def iniciar_programa():
    """Bucle principal con el menú."""
    while True:
        print("MENÚ POKÉDEX")
        print("1. Agregar Pokémon")
        print("2. Ver Pokédex")
        print("3. Eliminar Pokémon")
        print("4. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == '1':
            agregar_pokemon()
        elif opcion == '2':
            ver_pokemones()
        elif opcion == '3':
            eliminar_pokemon()
        elif opcion == '4':
            print("\n¡Adiós!")
            break  # Rompe el bucle para terminar el programa
        else:
            print("Opción no válida. Inténtalo de nuevo.")
if __name__ == "__main__":
    iniciar_programa()