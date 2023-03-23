# input

import random
# processing

def juego():
    opciones = ["Piedra", "Papel", "Tijera"]
    jugador = input("Elige Piedra, Papel o Tijera: ").capitalize()
    computadora = random.choice(opciones)
    print(f"La computadora eligió {computadora}")
    if jugador == computadora:
        print("Empate!")
    elif jugador == "Piedra":
        if computadora == "Papel":
            print("Perdiste!")
        else:
            print("Ganaste!")
    elif jugador == "Papel":
        if computadora == "Tijera":
            print("Perdiste!")
        else:
            print("Ganaste!")
    elif jugador == "Tijera":
        if computadora == "Piedra":
            print("Perdiste!")
        else:
            print("Ganaste!")
    else:
        print("Opción inválida. Por favor, elige Piedra, Papel o Tijera.")
    jugar_de_nuevo()

def jugar_de_nuevo():
    jugar = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar == "s":
        juego()
    elif jugar == "n":
        print("Gracias por jugar!")
    else:
        print("Opción inválida. Por favor, elige 's' para jugar de nuevo o 'n' para salir.")
        jugar_de_nuevo()

juego()