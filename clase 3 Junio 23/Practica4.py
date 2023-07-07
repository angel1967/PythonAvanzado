# Escribe una funcion llamada acumulador que tome un numero incial como
# parametro y devuelva otra funcion que pueda aumentar o disminuir el 
# numero acumulado por una cantidad dada.

def acumulador(num):
    acumulado = num

    def actualizar_cantidad(cantidad):
        nonlocal acumulado
        acumulado += cantidad
        return acumulado
    
    return actualizar_cantidad

acumulador_5 = acumulador(5)
print(acumulador_5(3))
