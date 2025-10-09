# --- Implementación de una Pila sin objetos ---

# Pila vacía
pila = []

# --- Funciones básicas ---
# Devuelve True si la pila está vacía, False en caso contrario.
def esta_vacia(pila):
    return len(pila) == 0

# Agrega un elemento al tope de la pila.
def apilar(pila, elemento):  # Push
    pila.append(elemento)
    print(f"Se apiló: {elemento}")


# Quita y retorna el elemento del tope de la pila.
# Si la pila está vacía, muestra un mensaje de error.
def desapilar(pila):  # Pop
    if not esta_vacia(pila):
        elemento = pila.pop()
        print(f"Se desapiló: {elemento}")
        return elemento
    else:
        print("La pila está vacía. No se puede desapilar.")


# Muestra y retorna el elemento en el tope de la pila sin quitarlo.
def ver_tope(pila):  # Peek
    if not esta_vacia(pila):
        print(f"Elemento en el tope: {pila[-1]}")
        return pila[-1]
    else:
        print("La pila está vacía.")


# Muestra el estado actual de la pila.
def mostrar_pila(pila):
    print("Estado actual de la pila:", pila)


# --- Ejemplo de uso de la pila paso a paso ---
print("¿La pila está vacía?", esta_vacia(pila))

apilar(pila, "Plato 1")
apilar(pila, "Plato 2")
apilar(pila, "Plato 3")
#i
mostrar_pila(pila)
ver_tope(pila)

desapilar(pila)
mostrar_pila(pila)

desapilar(pila)
desapilar(pila)
desapilar(pila)  # Intento extra

print("¿La pila está vacía?", esta_vacia(pila))
