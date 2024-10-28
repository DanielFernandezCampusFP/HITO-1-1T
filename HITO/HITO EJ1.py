# Definimos una función para mostrar el menú de opciones:
def mostrar_menu():
    print("MENU:")
    print("Seleccione la figura que quiera calcular, hecho por Daniel Fernández Carrero")  
    print("1 - Cuadrado") 
    print("2 - Rectángulo")  
    print("3 - Salir")  

# Definimos una función para calcular el área y perímetro de un cuadrado:
def calcular_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))  
    area = lado ** 2  
    perimetro = 4 * lado  
    print("Figura: Cuadrado")  
    print("Área:", area)  
    print("Perímetro:", perimetro)  

# Definimos una función para calcular el área y perímetro de un rectángulo:
def calcular_rectangulo():
    base = float(input("Introduce la base del rectángulo: "))  
    altura = float(input("Introduce la altura del rectángulo: "))  
    area = base * altura  
    perimetro = 2 * (base + altura) 
    print("Figura: Rectángulo")  
    print("Área:", area)  
    print("Perímetro:", perimetro)    

# Bucle principal para mostrar el menú y recibir la opción del usuario:
while True:
    mostrar_menu()  
    opcion = int(input("Selecciona una opción: "))  
    if opcion == 1:
        calcular_cuadrado()  
    elif opcion == 2:
        calcular_rectangulo()  
    elif opcion == 3:
        print("Saliendo del programa... Hasta luego")  
        print("Hecho por: Daniel Fernández Carrero")  
        break 
    else:
        print("Opción no válida. Por favor, intente de nuevo con un término válido.")  
