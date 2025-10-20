# Lider: Fernando Mejia
# Adalid Bahena
# Jesús Bolaños
# Alexis Beltran
# Estrada Romero
# Darío Emiliano

#Importaciones y configuración básica - Fernando
from flask import Flask, render_template, request, jsonify, redirect, url_for
import random
import json
import os

app = Flask(_name_)

DATA_FILE="data.json"

#Función cargar_datos() - Dario
def cargar_datos():
    if not os.path.exists(DATA_FILE):
        datos = {"puntos": 0, "intentos": 0, "numero": random.randint(1, 100)}
        guardar_datos(datos)
    else:
        with open(DATA_FILE, "r") as f:
            datos = json.load(f)
    return datos

#Funciones para manejar el juego - Adalid y Fernando
def guardar_datos(datos):
    with open(DATA_FILE, "w") as f:
        json.dump(datos, f)

def reiniciar_juego():
    datos = {"puntos": 0, "intentos": 0, "numero": random.randint(1, 100)}
    guardar_datos(datos)
    return datos

def nuevo_numero():
    datos = cargar_datos()
    datos["numero"] = random.randint(1, 100)
    guardar_datos(datos)
return datos

#Ruta principal (/) - Jesús
@app.route('/')
def index():
    datos = cargar_datos()
    return render_template('index.html', puntos=datos["puntos"], intentos=datos["intentos"])

#Ruta /adivinar - Alexis y Angeles
@app.route('/adivinar', methods=['POST'])
def adivinar():
    datos = cargar_datos()
    numero_usuario = int(request.form['numero'])
    numero_correcto = datos["numero"]
    datos["intentos"] += 1

    if numero_usuario == numero_correcto:
        datos["puntos"] += 100
        mensaje = f"¡Adivinaste! El número era {numero_correcto}. +100 puntos"
        nuevo_numero()
    else:
        mensaje = f"No era {numero_usuario}. El número correcto era {numero_correcto}."
        nuevo_numero()

    guardar_datos(datos)
    return render_template('resultado.html', mensaje=mensaje, puntos=datos["puntos"], intentos=datos["intentos"])


