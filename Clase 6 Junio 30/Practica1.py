# Ejercicio 1
# Crea un archivo de texto.txt con varias lineas en la misma carpeta
# de Python que estás trabajando.
# - crea una funcion que reciba 2 argumentos: El nombre del archivo a leer
# y el nombre del nuevo archivo.
# - La funcion debe leer el archivo de texto, ordenar las lineas alfabeticamente
# y guardar el resultado en otro archivo.

def ordenar_lineas(archivo_entrada, archivo_salida):
    try:
        # Abrir el archivo de entrada en modo lectura
        with open(archivo_entrada, 'r') as file_in:
            # Leer todas las líneas del archivo de entrada
            lineas = file_in.readlines()
        
        # Ordenar las líneas alfabéticamente
        lineas_ordenadas = sorted(lineas)
        
        # Abrir el archivo de salida en modo escritura
        with open(archivo_salida, 'w') as file_out:
            # Escribir las líneas ordenadas en el archivo de salida
            file_out.writelines(lineas_ordenadas)
        
        print("Líneas ordenadas y guardadas exitosamente en el archivo secundario.txt.")
    
    except FileNotFoundError:
        print("El archivo de entrada no fue encontrado.")
    
    except Exception as e:
        print("Error al ordenar y guardar las líneas:", str(e))

# Ejemplo de uso de la función
ordenar_lineas("primario.txt", "secundario.txt")
