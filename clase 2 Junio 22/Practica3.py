# Crear una función llamada obtener_promedio que acepte una lista 
# de números como argumento y retorne el promedio de dichos números.

def obtener_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

numeros = [22, 4, 16, 28, 10]
promedio = obtener_promedio(numeros)
print(promedio)
