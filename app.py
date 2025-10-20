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