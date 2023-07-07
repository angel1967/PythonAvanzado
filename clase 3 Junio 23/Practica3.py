#Escribe una funcion llamada generador_potencias que tome un numero
# como parametro y devuelva otra funcion que pueda calcular la potencia
# de ese numero elevado a un exponente dado.

def gener_pot(base):
    def potencia(exponente):
        return base ** exponente
    return potencia

base_2 = gener_pot(2)
print(base_2(6))
