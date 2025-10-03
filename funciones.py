def validar_legajo(lista: list, numero_legajo: int) -> bool:
    resultado = False
    for i in range(len(lista)):
        if numero_legajo == lista[i]:
            resultado = True

    return resultado

def crear_matriz(filas: int, columnas: int, valor_inicial = 0) -> list:
    matriz = []
    for _ in range(filas):
        una_fila = [valor_inicial] * columnas
        matriz += [una_fila]
    
    return matriz

def mostrar_matriz(matriz: list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:<4}", end = " ")
        print()

def cargar_matriz(matriz: list, fila: int, columna: int, recaudacion: int):
    matriz[fila][columna] += recaudacion

def pedir_numero(mensaje: str, mensaje_error: str) -> int|None:
    numero = int(input(mensaje))
    while type(numero) != int:
        numero = None
        print(mensaje_error)
        numero = int(input(mensaje))
    return numero

numero = pedir_numero("Ingrese un número: ", "Error...")