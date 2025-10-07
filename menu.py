import os
from funciones import *

def main():
    legajos = [12, 24, 33, 11, 50, 13, 78, 82, 37, 65, 10, 73, 90, 28, 45]
    # matriz = crear_matriz(3, 5)
    matriz = [[1, 2, 3 , 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15]]

    while True:
        opcion = input("1.Cargar planilla de recaudación\n2.Mostrar recaudación de cada coche y línea \n3.Calcular y mostrar la recaudación por línea \n4.Calcular y mostrar la recaudación por coche \n5.Calcular y mostrar la recaudación total \n6.Salir \nElige una opción: ")

        match opcion:
            case "1":
                numero_legajo = int(input("Ingrese el legajo: ")) 
                validacion = validar_legajo(legajos, numero_legajo)
                seguir = "si"
                while validacion == True and seguir == "si":
                    recaudacion_ingresada = int(input("Ingrese la recaudación: "))
                    linea = int(input("Ingrese el número de la linea: "))
                    coche = int(input("Ingrese el número de coche: "))
                    cargar_matriz(matriz, linea, coche, recaudacion_ingresada)
                    seguir = input("Desea ingresar otra recaudación? si/no: ")
            case "2":
                mostrar_matriz(matriz)
            case "3":
                total_lineas = calcular_recaudacion_por_linea(matriz)
                print(f"La recaudacion por línea es:{total_lineas}")
            case "4":
                numero_coche = int(input("Ingrese el numero de coche (0-4): ")) 
                total_coche = calcular_recaudacion_por_coche(matriz, numero_coche)
                print(f"La recaudacion del coche es:{total_coche}")
            case "5":
                recaudacion_total = calcular_recaudacion_total(matriz)
                print(f"La recaudacion total es de:{recaudacion_total}") 
            case "6":
                print("Saliendo del programa")
                break
                

        os.system("pause")
        os.system("cls")

if __name__ == "__main__":
    main()


