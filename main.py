from os import system
from functions import *
import time as tm

#Permite limpiar la pantalla de lo que antes del system("clear/cls").
system("clear")

print("Este es un código para simular una especie de ChatBot, para practicar para el Bothaton.\nCon esto, servira para practicar lo básico y esencial de Python hasta cosas más complejas que se irán comentando en el código.")

tm.sleep(10)
system("clear")

usuarios = registrarUsuarios()
mostrarUsuarios(usuarios)