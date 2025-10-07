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
    while type(numero) != int or numero < 0:
        numero = None
        print(mensaje_error)
        numero = int(input(mensaje))
    return numero

def verificar_tipo_entero(matriz: list, valor_inicial = 0) -> bool:
    bandera = True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if type(matriz[i][j]) != int and type(matriz[i][j]) != valor_inicial:
                bandera = False
                break
    
    return bandera

def validar_rango_filas(matriz: list, inicio: int, fin: int) -> bool:
    bandera = False
    for i in range(len(matriz)):
        if i >= inicio and i <= fin:
            bandera = True

    return bandera

def validar_rango_columnas(matriz: list, inicio: int, fin: int) -> bool:
    bandera = True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j >= inicio and j <= fin:
                bandera = True

    return bandera

def calcular_recaudacion_por_linea(matriz: list) -> list:
    totales_linea = []
    if verificar_tipo_entero(matriz) == True and validar_rango_filas(matriz, 1, 3) == True:
        for fila in matriz:
            total = sum(fila)
            totales_linea += [total]
    return totales_linea

def calcular_recaudacion_por_coche(matriz: list) -> list:
    columnas = len(matriz[0])
    totales_coche = [0] * columnas
    if verificar_tipo_entero(matriz) == True and validar_rango_columnas(matriz, 0, 4) == True:
        for j in range(columnas):
            totales_coche[j] = sum(matriz[i][j] for i in range(len(matriz)))
    return totales_coche

def calcular_recaudacion_total(matriz: list) -> int:
    total = sum(sum(fila) for fila in matriz)
    return total
