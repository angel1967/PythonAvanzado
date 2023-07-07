# Crea una función llamada actualizar_diccionario que acepte un
# diccionario y un conjunto de argumentos keyword, y actualice 
# el diccionario con los nuevos pares clave-valor proporcionados

def actualizar_diccionario(diccionario, **kwargs):
    diccionario.update(kwargs)
    return diccionario

mi_diccionario = {'nombre': 'John', 'edad': 25}
nuevos_datos = {'ciudad': 'Nueva York', 'ocupacion': 'Programador'}

diccionario_actualizado = actualizar_diccionario(mi_diccionario, **nuevos_datos)
print(diccionario_actualizado)
