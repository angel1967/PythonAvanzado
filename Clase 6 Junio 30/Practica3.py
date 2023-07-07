# Utiliza la funcion open y json.dumps para convertir un diccionario en formato JSON
# y guardar el archivo.
# {"nombre":"juan","edad":30,"ciudad":"México"}

import json

def guardar_diccionario_como_json(diccionario, nombre_archivo):
    try:
        # Convertir el diccionario a formato JSON
        json_data = json.dumps(diccionario)
        
        # Abrir el archivo en modo escritura
        with open(nombre_archivo, 'w') as file:
            # Escribir el contenido JSON en el archivo
            file.write(json_data)
        
        print("Diccionario guardado exitosamente como archivo JSON:", nombre_archivo)
    
    except Exception as e:
        print("Error al guardar el diccionario como archivo JSON:", str(e))

# Ejemplo de uso
diccionario = {"nombre": "juan", "edad": 30, "ciudad": "Mexico"}
nombre_archivo = "diccionario.json"

guardar_diccionario_como_json(diccionario, nombre_archivo)
