import random # Importamos la librería random para generar valores aleatorios
# Definimos una función para el juego Piedra, Papel o Tijera
def jugar_piedra_papel_tijera():
    opciones = ["Piedra", "Papel", "Tijera"]  
    usuario_puntaje = 0 
    maquina_puntaje = 0  

    # Bucle para jugar hasta que uno de los jugadores gane 3 veces
    while usuario_puntaje < 3 and maquina_puntaje < 3:
        try:
            usuario_opcion = int(input("Elige una opción: 1 - Piedra, 2 - Papel, 3 - Tijera: Hecho por Daniel Fernández ")) - 1 
            if usuario_opcion not in [0, 1, 2]: 
                print("Opción no válida. Prueba de nuevo con otra cosa.")
        except ValueError:
                print("Por favor, introduce un número válido.")  
                continue  

        maquina_opcion = random.randint(0, 2) 
        print(f"Has elegido: {opciones[usuario_opcion]}")  
        print(f"La máquina ha elegido: {opciones[maquina_opcion]}")  

        # Verificamos el resultado del juego
        if usuario_opcion == maquina_opcion:
            print("Empate!")  
        elif (usuario_opcion == 0 and maquina_opcion == 2) or \
             (usuario_opcion == 1 and maquina_opcion == 0) or \
             (usuario_opcion == 2 and maquina_opcion == 1):
            print("Has GANADO!")  
            usuario_puntaje += 1  
        else:
            print("Has perdido, inténtalo de nuevo.")  
            maquina_puntaje += 1   
        print(f"Puntaje - Tú: {usuario_puntaje}, Máquina: {maquina_puntaje}")  

    # Mensaje final del juego
    if usuario_puntaje == 3:
        print("Felicidades, HAS GANADO! (Hecho por Daniel Fernández")  # Mensaje si el usuario gana
    else:
        print("Lo siento, has perdido, prueba de nuevo! Hecho por Daniel Fernández.")  # Mensaje si la máquina gana
