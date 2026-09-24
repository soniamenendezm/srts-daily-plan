import json
import numpy as np

# Carga del JSON desde el archivo local
with open('./datosPaciente.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

n_dias = 13  # Número de días de rehabilitación
sesiones = np.arange(1, n_dias + 1)

# Función para generar datos simulados
def generar_datos_evolucion(punto_partida, sesiones, tendencia=0.05, ruido=5):
    # La tendencia positiva representa la mejora de la magnitud a lo largo del tiempo
    # El ruido añade variabilidad a los datos simulados
    mejora = tendencia * sesiones + punto_partida
    ruido_random = np.random.normal(0, ruido, size=sesiones.shape)
    return mejora + ruido_random


datos_altura_maxima = {
    "ejercicio001": generar_datos_evolucion(1, sesiones, tendencia=0.2, ruido=0.05),
    "ejercicio002": generar_datos_evolucion(1, sesiones, tendencia=0.25, ruido=0.05),
    "ejercicio003": generar_datos_evolucion(1, sesiones, tendencia=0.15, ruido=0.05),
    "ejercicio004": generar_datos_evolucion(1, sesiones, tendencia=0.18, ruido=0.05),
    "ejercicio005": generar_datos_evolucion(1, sesiones, tendencia=0.18, ruido=0.05),
    "ejercicio006": generar_datos_evolucion(1, sesiones, tendencia=0.15, ruido=0.05),
    "ejercicio007": generar_datos_evolucion(1, sesiones, tendencia=0.17, ruido=0.05),
    "ejercicio008": generar_datos_evolucion(1, sesiones, tendencia=0.19, ruido=0.05),
    "ejercicio009": generar_datos_evolucion(1, sesiones, tendencia=0.2, ruido=0.05),
}

"""
import matplotlib.pyplot as plt

y = datos_altura_maxima['ejercicio001']
x = np.arange(13)
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.show()
"""
# Iterar sobre las sesiones y ejercicios para actualizar los valores
for sesion in datos.get("sesiones", []):
    for ejercicio in sesion.get("ejercicios", []):
        id_ejercicio = ejercicio.get("idEjercicio")
        if id_ejercicio in datos_altura_maxima:
            ejercicio["alturaMaxima"] = datos_altura_maxima[id_ejercicio][0]
            datos_altura_maxima[id_ejercicio] = datos_altura_maxima[id_ejercicio][1:]


datos_profundidad_maxima = {
    "ejercicio001": generar_datos_evolucion(23, sesiones, tendencia=0.12, ruido=0.05),
    "ejercicio002": generar_datos_evolucion(23, sesiones, tendencia=0.14, ruido=0.05),
    "ejercicio003": generar_datos_evolucion(23, sesiones, tendencia=0.115, ruido=0.05),
    "ejercicio004": generar_datos_evolucion(23, sesiones, tendencia=0.14, ruido=0.05),
    "ejercicio005": generar_datos_evolucion(23, sesiones, tendencia=0.132, ruido=0.05),
    "ejercicio006": generar_datos_evolucion(23, sesiones, tendencia=0.13, ruido=0.05),
    "ejercicio007": generar_datos_evolucion(23, sesiones, tendencia=0.17, ruido=0.05),
    "ejercicio008": generar_datos_evolucion(23, sesiones, tendencia=0.12, ruido=0.05),
    "ejercicio009": generar_datos_evolucion(23, sesiones, tendencia=0.12, ruido=0.05),
}

# Iterar sobre las sesiones y ejercicios para actualizar los valores
for sesion in datos.get("sesiones", []):
    for ejercicio in sesion.get("ejercicios", []):
        id_ejercicio = ejercicio.get("idEjercicio")
        if id_ejercicio in datos_profundidad_maxima:
            ejercicio["profundidadMaxima"] = datos_profundidad_maxima[id_ejercicio][0]
            datos_profundidad_maxima[id_ejercicio] = datos_profundidad_maxima[id_ejercicio][1:]


datos_angulo_maximo = {
    "ejercicio001": generar_datos_evolucion(20, sesiones, tendencia=0.22, ruido=0.05),
    "ejercicio002": generar_datos_evolucion(20, sesiones, tendencia=0.14, ruido=0.05),
    "ejercicio003": generar_datos_evolucion(20, sesiones, tendencia=0.15, ruido=0.05),
    "ejercicio004": generar_datos_evolucion(20, sesiones, tendencia=0.23, ruido=0.05),
    "ejercicio005": generar_datos_evolucion(20, sesiones, tendencia=0.12, ruido=0.05),
    "ejercicio006": generar_datos_evolucion(20, sesiones, tendencia=0.15, ruido=0.05),
    "ejercicio007": generar_datos_evolucion(20, sesiones, tendencia=0.17, ruido=0.05),
    "ejercicio008": generar_datos_evolucion(20, sesiones, tendencia=0.16, ruido=0.05),
    "ejercicio009": generar_datos_evolucion(20, sesiones, tendencia=0.18, ruido=0.05),
}

# Iterar sobre las sesiones y ejercicios para actualizar los valores
for sesion in datos.get("sesiones", []):
    for ejercicio in sesion.get("ejercicios", []):
        id_ejercicio = ejercicio.get("idEjercicio")
        if id_ejercicio in datos_angulo_maximo:
            ejercicio["anguloMaximo"] = datos_angulo_maximo[id_ejercicio][0]
            datos_angulo_maximo[id_ejercicio] = datos_angulo_maximo[id_ejercicio][1:]


datos_fuerza = {
    "ejercicio001": generar_datos_evolucion(26, sesiones, tendencia=0.15, ruido=0.05),
    "ejercicio002": generar_datos_evolucion(26, sesiones, tendencia=0.13, ruido=0.05),
    "ejercicio003": generar_datos_evolucion(26, sesiones, tendencia=0.15, ruido=0.05),
    "ejercicio004": generar_datos_evolucion(26, sesiones, tendencia=0.18, ruido=0.05),
    "ejercicio005": generar_datos_evolucion(26, sesiones, tendencia=0.25, ruido=0.05),
    "ejercicio006": generar_datos_evolucion(26, sesiones, tendencia=0.12, ruido=0.05),
    "ejercicio007": generar_datos_evolucion(26, sesiones, tendencia=0.17, ruido=0.05),
    "ejercicio008": generar_datos_evolucion(26, sesiones, tendencia=0.26, ruido=0.05),
    "ejercicio009": generar_datos_evolucion(26, sesiones, tendencia=0.27, ruido=0.05),
}

# Iterar sobre las sesiones y ejercicios para actualizar los valores
for sesion in datos.get("sesiones", []):
    for ejercicio in sesion.get("ejercicios", []):
        id_ejercicio = ejercicio.get("idEjercicio")
        if id_ejercicio in datos_fuerza:
            ejercicio["fuerzaMaxima"] = datos_fuerza[id_ejercicio][0]
            datos_fuerza[id_ejercicio] = datos_fuerza[id_ejercicio][1:]


datos_velocidad = {
    "ejercicio001": generar_datos_evolucion(50, sesiones, tendencia=0.2, ruido=0.05),
    "ejercicio002": generar_datos_evolucion(50, sesiones, tendencia=0.25, ruido=0.05),
    "ejercicio003": generar_datos_evolucion(50, sesiones, tendencia=0.15, ruido=0.05),
    "ejercicio004": generar_datos_evolucion(50, sesiones, tendencia=0.18, ruido=0.05),
    "ejercicio005": generar_datos_evolucion(50, sesiones, tendencia=0.18, ruido=0.05),
    "ejercicio006": generar_datos_evolucion(50, sesiones, tendencia=0.15, ruido=0.05),
    "ejercicio007": generar_datos_evolucion(50, sesiones, tendencia=0.17, ruido=0.05),
    "ejercicio008": generar_datos_evolucion(50, sesiones, tendencia=0.19, ruido=0.05),
    "ejercicio009": generar_datos_evolucion(50, sesiones, tendencia=0.2, ruido=0.05),
}

# Iterar sobre las sesiones y ejercicios para actualizar los valores
for sesion in datos.get("sesiones", []):
    for ejercicio in sesion.get("ejercicios", []):
        id_ejercicio = ejercicio.get("idEjercicio")
        if id_ejercicio in datos_velocidad:
            ejercicio["velocidadMaxima"] = datos_velocidad[id_ejercicio][0]
            datos_velocidad[id_ejercicio] = datos_velocidad[id_ejercicio][1:]


# Guardar los cambios de vuelta en el archivo JSON
with open('C:/SONIA/4 ANO UNIVERSIDAD/Proyectos/datosPaciente.json', 'w', encoding='utf-8') as archivo:
    json.dump(datos, archivo, indent=4, ensure_ascii=False)

print("Datos actualizados correctamente.")


