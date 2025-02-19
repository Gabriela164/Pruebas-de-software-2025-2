
''''
Script que suma dos números enteros 
Prueba para Pruebas de Software y administración de la configuración

Febrero 2025 
Autor: Gabriela164
'''

def suma(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int,float)):
        return "Error: ambos valores deben ser números"
    return a + b

print("La suma de 3 y 5 es: ", suma("2","1"))

















