import random

def obtener_palabra_secreta():
    palabras = ['python', 'ahorcado', 'programacion', 'databricks', 'espacio']
    return random.choice(palabras)

def mostrar_estado(palabra, letras_adivinadas, intentos_restantes):
    # Construye la vista con _ para letras no adivinadas
    estado = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            estado += letra + ' '
        else:
            estado += '_ '
    estado = estado.strip()
    print(f"\nPalabra: {estado}")
    print(f"Intentos restantes: {intentos_restantes}")
    print(f"Letras usadas: {', '.join(sorted(letras_adivinadas))}\n")

def obtener_letra_usuario(letras_adivinadas):
    while True:
        letra = input("Adivina una letra: ").strip().lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, introduce una sola letra.")
        elif letra in letras_adivinadas:
            print("Ya probaste esa letra. Elige otra.")
        else:
            return letra

def jugar_ahorcado():
    palabra = obtener_palabra_secreta()
    letras_adivinadas = []       # Lista en lugar de set
    intentos_restantes = 6
    ganado = False

    print("¡Bienvenido al Ahorcado!")

    while intentos_restantes > 0:
        mostrar_estado(palabra, letras_adivinadas, intentos_restantes)
        letra = obtener_letra_usuario(letras_adivinadas)
        letras_adivinadas.append(letra)

        if letra in palabra:
            print("¡Bien! La letra está en la palabra.")
        else:
            intentos_restantes -= 1
            print("Oh no… esa letra no está.")

        # Comprueba si ya has adivinado toda la palabra
        completa = True
        for caracter in palabra:
            if caracter not in letras_adivinadas:
                completa = False
                break

        if completa:
            print(f"\n🎉 ¡Felicidades! Has adivinado la palabra: {palabra}")
            ganado = True
            break  # sale del bucle al ganar

    if not ganado:
        print(f"\n☠️  ¡Se acabaron los intentos! La palabra era: {palabra}")

jugar_ahorcado()