class nodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None #apunta al siguiente nodo
        self.anterior = None  #apunta al nodo anterior

nodo1 = nodoDoble(10)
nodo2 = nodoDoble(20)
nodo3 = nodoDoble(30)
nodo1.siguiente = nodo2 
nodo2.anterior = nodo1  
nodo2.siguiente = nodo3 
nodo3.anterior = nodo2  
cabeza = nodo1
current = cabeza
while current:
    print(current.dato, end=" <-> ")
    current=current.siguiente
print("None")
current = cabeza
while current.siguiente:
    current=current.siguiente
while current:
    print(current.dato, end=" <-> ")
    current=current.anterior
print("None")
Actualizacion
