# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 10:31:02 2023

@author: joan camilo tamayo
"""
import time
from datetime import datetime
import random
from github import Github
from github import InputGitTreeElement

# Configuración de autenticación
token = 'Hello :)'  # Reemplaza con tu token de acceso personal
repository_name = 'prueba'  # Reemplaza con el nombre de tu repositorio

# Inicialización de la instancia de Github
g = Github(token)
repo = g.get_user().get_repo(repository_name)

# Función para enviar una actualización al repositorio
def enviar_actualizacion():
    # Crear un archivo y enviarlo al repositorio
    contenido = f"Esta es una actualización automática generada el {datetime.now()}."
    archivo = f"actualizacion_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    repo.create_file(archivo, "Actualización automática", contenido)


# actualizaciones diarias de forma aleatoria
while True:
    actualizaciones_diarias = random.randint(1, 10)  # Generar un número aleatorio de actualizaciones (entre 1 y 10)
    for _ in range(actualizaciones_diarias):
        try:
            enviar_actualizacion()
        except Exception as e:
            print(f"Error al enviar la actualización: {str(e)}")
    tiempo_espera = random.randint(1, 24) * 3600  # Esperar entre 1 y 24 horas para enviar la siguiente serie de actualizaciones
    time.sleep(tiempo_espera)