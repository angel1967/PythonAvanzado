# Escribe una función llamada contador que devuelva otra funcion.
# la funcio devuelta debe contar cuantas veces ha sido llamad y mostrar
# el resultado.


def contador():
    count = 0  # Variable para contar las llamadas

    def contar():
        nonlocal count  # Acceder a la variable count fuera del ámbito actual
        count += 1
        print("La función ha sido llamada", count, "veces.")

    return contar

c = contador()  # Crear una instancia de la función contador

c()  # Llamar a la función devuelta por contador
# Salida: La función ha sido llamada 1 veces.

c()  # Llamar a la función devuelta nuevamente
# Salida: La función ha sido llamada 2 veces.

c()  # Llamar a la función devuelta una vez más
# Salida: La función ha sido llamada 3 veces.
