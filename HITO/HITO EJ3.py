# Definimos la función para manejar una cuenta bancaria
def cuenta_bancaria():
    saldo = float(input("Introduce el saldo inicial: "))  
    ingresos = 0 
    retiradas = 0  
    
    while saldo < 0:  # Validamos que el saldo inicial no sea negativo
        print("El saldo inicial no puede ser negativo.")  # Mensaje de error si el saldo es negativo
        saldo = float(input("Introduce el saldo inicial: "))  # Solicitamos nuevamente el saldo inicial
    
    # Bucle principal del programa
    while True:
        print("\nSeleccione una opción:")
        print("1 - Ingresar dinero")
        print("2 - Retirar dinero")
        print("3 - Mostrar saldo")
        print("4 - Estadísticas")
        print("5 - Salir")
        
        opcion = int(input("Opción: "))  # Solicitamos la opción del menú al usuario
        
        if opcion == 1:
            ingreso = float(input("Cantidad a ingresar: "))  # Solicitamos la cantidad a ingresar
            if ingreso > 0: 
                saldo += ingreso  
                ingresos += 1  
                print(f"Ingresaste: {ingreso}. Nuevo saldo: {saldo}")  # Mostramos el saldo actualizado
            else:
                print("No se puede ingresar una cantidad negativa.")  # Error si la cantidad es negativa
           

        elif opcion == 2:
            retiro = float(input("Cantidad a retirar: "))  # Solicitamos la cantidad a retirar
            if 0 < retiro <= saldo:  
                saldo -= retiro 
                retiradas += 1 
                print(f"Retiraste: {retiro}. Nuevo saldo: {saldo}")  
            else:
                print("Cantidad no válida o saldo insuficiente.")
         
        elif opcion == 3:
            print(f"Saldo actual: {saldo}")  
             
        elif opcion == 4:
            print(f"Estadísticas: Ingresos - {ingresos}, Retiros - {retiradas}")  # Mostramos las estadísticas
          

        elif opcion == 5:
            print("Saliendo del programa...")  # Mensaje de salida
            break  
        
        else:
            print("Opción no válida. Intente nuevamente.")  # Mensaje de error si la opción no es válida
