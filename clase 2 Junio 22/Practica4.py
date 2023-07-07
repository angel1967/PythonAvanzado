# Utilizar la libreria statistics.
# Crea una función llamada calcular_estadisticas que acepte una 
# lista de números y un numero variable de argumentos keyword. 
# Los argumentos keyword pueden ser “media”, “mediana” y
# “desviacion_estandar”. La función debe calcular las estadísticas 
# indicadas en los argumentos keyword y retornar un diccionario con
# los resultados.

import statistics

def calcular_estadisticas(lista, **kwargs):
    resultados = {}

    if 'media' in kwargs:
        media = statistics.mean(lista)
        resultados['media'] = media

    if 'mediana' in kwargs:
        mediana = statistics.median(lista)
        resultados['mediana'] = mediana

    if 'desviacion_estandar' in kwargs:
        desviacion = statistics.stdev(lista)
        resultados['desviacion_estandar'] = desviacion

    return resultados

numeros = [42, 4, 6, 8, 10]

resultados = calcular_estadisticas(numeros, media=True, mediana=True, desviacion_estandar=True)
print(resultados)
