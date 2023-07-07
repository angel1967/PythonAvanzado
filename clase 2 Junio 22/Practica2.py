# Implementa una función llamada sumar_elementos que tome un 
# numero variable de argumentos y retorne la suma de todos ellos.

def sumar_elementos(*args):
    suma = sum(args)
    return suma

resultado = sumar_elementos(1, 2, 23, 14, 5)
print(resultado)
