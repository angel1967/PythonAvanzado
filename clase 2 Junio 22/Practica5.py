# Implementa una función llamada duplicar_lista que tome una lista
# como argumento y retorne una nueva lista con los elementos duplicados

def duplicar_lista(lista):
    nueva_lista = lista * 2
    return nueva_lista

mi_lista = [1, 2, 3, 4, 5]
lista_duplicada = duplicar_lista(mi_lista)
print(lista_duplicada)
