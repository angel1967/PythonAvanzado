# Dada la siguiente lista de listas 
# "lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]" 
# calcula la suma de los elementos de la lista individualmente 
# y regresar [6, 15 y 24]"


lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sumas = [sum(sublista) for sublista in lista_de_listas]

print(sumas)