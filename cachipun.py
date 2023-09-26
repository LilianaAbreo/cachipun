import random

""" este modulo juega cachipun"""
opciones = ["piedra", "papel", "tijera"]
#lista de las opciones 
def juego_cachipun(humano,computador): 
    #inicia el juego
    while  humano not in opciones:
        print("valor invalido: escriba un valor entre piedra, papel o tijera")
        humano = input("Ingrese la jugada: ")
        humano = humano.lower()
    print("El jugador eligio: ",humano)
    print("La computadora eligio:  " ,computador)
    if (humano=="papel" and computador=="piedra" ) or (humano=="tijera" and computador=="papel") or (humano=="piedra" and computador=="tijera"):
        print("TU ERES EL GANADOR")
    elif humano==computador:
        print("ES UN EMPATE VUELVE A JUGAR PARA GANAR")
    else: 
        print("GANO LA COMPUTADORA")
    print("el juego termino")



if __name__=="__main__":
    print("Bienvenido al juego Cachipún contra el computador")
    print("Opciones: piedra, papel, tijera")
    opciones= ["piedra","papel","tijera"]
    humano = input("Ingrese su jugada: ")
    humano= humano.lower()
    #Entrada del jugador
    computador=random.choice(opciones)
    #Entrada del computador
    #Se invoca al modulo cachipun y su función
    result= juego_cachipun(humano, computador)
    print(result)
