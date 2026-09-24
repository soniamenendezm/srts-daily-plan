import pandas as pd
import numpy as np
import json
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import random

# Ruta al archivo JSON
ruta_archivo = './datosPaciente.json'    

# Cargar el archivo JSON
with open(ruta_archivo, 'r', encoding='utf-8') as file:
    datos_paciente = json.load(file)

# Extraer las sesiones y convertirlas en una lista para el DataFrame
sesiones = datos_paciente["sesiones"]
data = []

for sesion in sesiones:
    for ejercicio in sesion["ejercicios"]:
        data.append({
            "sesion": sesion["sesion"],
            "fecha": sesion["fecha"],
            "idEjercicio": ejercicio["idEjercicio"],
            "nombreEjercicio": ejercicio["nombreEjercicio"],
            "clasificacionEjercicio": ejercicio["clasificacionEjercicio"],
            "anguloMaximo": ejercicio["anguloMaximo"],
            "fuerzaMaxima": ejercicio["fuerzaMaxima"],
            "alturaMaxima": ejercicio["alturaMaxima"],
            "profundidadMaxima": ejercicio["profundidadMaxima"],
            "velocidadMaxima": ejercicio["velocidadMaxima"],
            "duracion": ejercicio["duracion"],
            "calificacion": ejercicio["calificacion"],
            "comentarios": ejercicio["comentarios"]
        })

# Crear el DataFrame
df = pd.DataFrame(data)
df = df.drop(['fecha', 'nombreEjercicio', 'comentarios', 'duracion'], axis=1)  # Quitar columnas no necesarias

df_ejercicio001 = df[df['idEjercicio'] == 'ejercicio001']
df_ejercicio002 = df[df['idEjercicio'] == 'ejercicio002']
df_ejercicio003 = df[df['idEjercicio'] == 'ejercicio003']
df_ejercicio004 = df[df['idEjercicio'] == 'ejercicio004']
df_ejercicio005 = df[df['idEjercicio'] == 'ejercicio005']
df_ejercicio006 = df[df['idEjercicio'] == 'ejercicio006']
df_ejercicio007 = df[df['idEjercicio'] == 'ejercicio007']
df_ejercicio008 = df[df['idEjercicio'] == 'ejercicio008']
df_ejercicio009 = df[df['idEjercicio'] == 'ejercicio009']

df_ejercicios = [df_ejercicio001, df_ejercicio002, df_ejercicio003, df_ejercicio004, df_ejercicio005, df_ejercicio006, df_ejercicio007, df_ejercicio008, df_ejercicio009]  # Lista de DataFrames para los ejercicios
metricas = ["anguloMaximo", "fuerzaMaxima", "alturaMaxima", "profundidadMaxima", "velocidadMaxima"]
ejercicios = ['ejercicio001', 'ejercicio002', 'ejercicio003', 'ejercicio004', 'ejercicio005','ejercicio006','ejercicio007', 'ejercicio008', 'ejercicio009']

# Crear el DataFrame df_coef para almacenar los coeficientes
df_coef = pd.DataFrame(columns=ejercicios, index=metricas)

# PASO 1

# Crear el modelo de regresión lineal
model = LinearRegression()

# Rellenar df_coef con los coeficientes de cada ejercicio y métrica
for i, ejercicio in enumerate(df_ejercicios):  # 'i' es el índice del ejercicio
    for j, metrica in enumerate(metricas):  # 'j' es el índice de la métrica
        y = ejercicio[metrica].values  # Convertir la columna a un array numpy
        x = np.arange(len(ejercicio)).reshape(-1, 1)  # Crear x y darle forma 2D

        # Ajustar el modelo de regresión
        model.fit(x, y)
        
        # Asignar el coeficiente a df_coef para la combinación ejercicio, métrica
        df_coef.iloc[j, i] = model.coef_[0]  # model.coef_ es un array, tomamos el primer valor

# Mostrar el DataFrame de los coeficientes
print(df_coef)


# PASO 2

ultima_sesion = df['sesion'].max()  
df_ultima_sesion = df[df['sesion'] == ultima_sesion]
#print(df_ultima_sesion)

media_metricas = {}

# Calcular la media de cada métrica en la última sesión
for metrica in metricas:
    media_metricas[metrica] = df_ultima_sesion[metrica].mean()

# Mostrar las medias
print("\nMedia de las métricas en la última sesión:")
print(media_metricas)


# Umbrales de cada métrica
altura_paciente = datos_paciente['altura']
normal_altura_máxima = altura_paciente*0.5 + altura_paciente*0.75
altura_maxima_umbral = normal_altura_máxima*0.8

diccionario_umbrales = {
    'anguloMaximo': 55,
    'fuerzaMaxima': 65,
    'alturaMaxima': altura_maxima_umbral,
    'profundidadMaxima': 70,
    'velocidadMaxima': 130
}

diferencias = {
    metrica: (valor - diccionario_umbrales[metrica]) 
    for metrica, valor in media_metricas.items()
}

# Filtrar y ordenar las métricas de menor a mayor según la diferencia
metricas_ordenadas = sorted(
    diferencias.keys(), 
    key=lambda metrica: diferencias[metrica]
)

metricas_por_mejorar = [
    metrica for metrica, valor in media_metricas.items()
    if valor < diccionario_umbrales[metrica]
]

# Mostrar la lista de métricas por mejorar
print("\nMétricas por mejorar:", metricas_por_mejorar, "")
print("Orden de mejora:", metricas_ordenadas, "\n")

plan_ejercicios = {}

for metrica in metricas_ordenadas:
    ejercicio_max = df_coef.loc[metrica].idxmax()
    valor_max = df_coef.loc[metrica].max()

    plan_ejercicios[metrica] = ejercicio_max

    # Mostrar el resultado
    print(f"El ejercicio con el coeficiente más alto en {metrica} es {ejercicio_max}")

print(plan_ejercicios)

plan_ejercicios_def = []

for i in metricas_por_mejorar:
    if len(plan_ejercicios_def) < 3:
        ejercicioSeleccionado = plan_ejercicios[i]
        if ejercicioSeleccionado not in plan_ejercicios_def:
            plan_ejercicios_def.append(ejercicioSeleccionado)
    metricas_ordenadas.remove(i)


for i in metricas_ordenadas:
    if len(plan_ejercicios_def) < 3:
        ejercicioSeleccionado = plan_ejercicios[i]
        if ejercicioSeleccionado not in plan_ejercicios_def:
            plan_ejercicios_def.append(ejercicioSeleccionado)

print("\nEjercicios del plan:", plan_ejercicios_def)

