# Utiliza la función filter y la función reduce para encontrar todas 
# las listas en una lista cuya lista de elementos sea mayor de un 
# cierto valor.
# Lista_de_listas = [[1,2,3], [4,5,6],[7,8,9]]
# valor = 10
# resultado: [[4,5,6], [7,8,9]]


from functools import reduce

Lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
valor = 10

resultado = list(filter(lambda x: reduce(lambda a, b: a + b, x) > valor, Lista_de_listas))
print(resultado)

