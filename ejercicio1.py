
alumnos = []


def registrar_alumno(nombre, edad, carrera):
   
    nuevo_alumno = {
        "nombre": nombre,
        "edad": int(edad), 
        "carrera": carrera
    }
    
    alumnos.append(nuevo_alumno)
print("--- Registro de Alumnos ---")
for i in range(3):
    print(f"\nDatos del Alumno #{i + 1}:")
    
    nombre = input("Ingresa el nombre: ")
    edad = input("Ingresa la edad: ") 
    carrera = input("Ingresa la carrera: ")
    
 
    registrar_alumno(nombre, edad, carrera)


print("\n--- Lista Final de Alumnos ---")
print(alumnos)