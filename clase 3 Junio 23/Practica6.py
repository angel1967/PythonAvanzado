#Escribe un programa que genere un patron de numeros en forma de piramide


altura = 10 

for i in range(altura):
    espacios = altura - i - 1
    ceros = 2 * i + 1
    print(' ' * espacios + '0' * ceros)
