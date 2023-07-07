# Dadas dos listas de igual longitud, crear un diccionario que contenga pares
# clave-valor combinando los elementos de ambas listas.
# Usa dict() y zip()

def crear_diccionario(lista_claves, lista_valores):
    if len(lista_claves) == len(lista_valores):
        diccionario = dict(zip(lista_claves, lista_valores))
        return diccionario
    else:
        print("Las listas no tienen la misma longitud.")

# Ejemplo de uso
claves = ['a', 'b', 'c', 'd']
valores = [1, 2, 3, 4]

diccionario_combinado = crear_diccionario(claves, valores)
print(diccionario_combinado)
