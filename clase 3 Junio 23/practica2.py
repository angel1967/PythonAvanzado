# Escribe una funcion llamada calculadora que tome dos numeros como 
# parametros y devuelva otra funcion que pueda realizar diferentes
# operaciones matematicas (suma, resta, multiplicacion y division)
# entre los dos numeros dados.

# Crear una instancia de la calculadora con los números 5 y 3
def calculadora(a,b):
    def suma():
        return a + b
    def resta():
        return a - b
    def multi():
        return a * b
    return {'suma':suma, 'resta':resta, 'multi':multi}

calc = calculadora(5, 30)

print(calc)
    