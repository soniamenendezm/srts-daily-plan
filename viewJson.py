import json
import numpy as np
import matplotlib.pyplot as plt

# Carga del JSON desde el archivo local
with open('./datosPaciente.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

lista = []

for sesion in datos.get("sesiones", []):
    for ejercicio in sesion.get("ejercicios", []):
        id_ejercicio = ejercicio.get("idEjercicio")
        if id_ejercicio == 'ejercicio007':
            lista.append(ejercicio["velocidadMaxima"])

plt.plot(range(len(lista)), lista, marker='o', linestyle='-', color='b', label='Altura máxima')
plt.show()