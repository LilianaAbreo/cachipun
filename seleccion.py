import random
""" seleciona la opcion entre (piedra, papel y tijera)"""
def seleccionar(): 
    opciones = ["piedra","papel","tijera"]
#esta son las opciones para el juego cachipun para poder jugar 
    element = random.choice(opciones)
    #para escoger elemento 
    return element

if __name__  == "__main__":
    seleccionar()
