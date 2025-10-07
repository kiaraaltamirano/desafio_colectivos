def validar_legajo(lista: list, numero_legajo: int) -> bool:
    """Valida que el número ingresado esté dentro del legajo
    Args:
        lista (list): Lista sobre la que se buscará el número
        numero_legajo (int): Número ingresado
    Returns:
        bool: Devuelve True si es válido, False en caso contrario
    """
    resultado = False
    for i in range(len(lista)):
        if numero_legajo == lista[i]:
            resultado = True

    return resultado

def crear_matriz(filas: int, columnas: int, valor_inicial = 0) -> list:
    """Crea una matriz
    Args:
        filas (int): Cantidad de filas que va a tener la matriz
        columnas (int): Cantidad de columnas que va a tener la matriz
        valor_inicial (int, optional): Valor base de los elementos de la lista,
        por default es 0.
    Returns:
        list: Devuelve la matriz creada
    """
    matriz = []
    for _ in range(filas):
        una_fila = [valor_inicial] * columnas
        matriz += [una_fila]
    
    return matriz

def mostrar_matriz(matriz: list):
    """Imprime una matriz por terminal
    Args:
        matriz (list): Matriz a mostrar
    No devuelve nada
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:<4}", end = " ")
        print()

def validar_rango(numero: int, inicio: int, fin: int) -> bool:
    """Valida un número dentro del rango deseado
    Args:
        numero (int): Número a validar
        inicio (int): Inicio del rango
        fin (int): Final del rango
    Returns:
        bool: True si el número es validado efectivamente, False en caso contrario
    """
    bandera = False
    if numero >= inicio and numero <= fin:
        resultado = True
    return bandera

def cargar_matriz(matriz: list, fila: int, columna: int, recaudacion: int):
    """Carga datos en una matriz determinada
    Args:
        matriz (list): Matriz a cargar
        fila (int): Fila en la que se almacenará el dato
        columna (int): Columna en la que se almacenará el dato
        recaudacion (int): Elemento a ser cargado
    No devuelve nada
    """
    if validar_rango(fila, 0, 2) == True and validar_rango(columna, 0, 4):
        matriz[fila][columna] += recaudacion

def pedir_numero(mensaje: str, mensaje_error: str) -> int|None:
    """Pide un número por consola
    Args:
        mensaje (str): Mensaje que se mostrará al pedir el número
        mensaje_error (str): Mensaje que se mostrará en caso de error
    Returns:
        int|None: Devuelve int si la validación es correcta, None en caso contrario
    """
    numero = int(input(mensaje))
    while type(numero) != int or numero < 0:
        numero = None
        print(mensaje_error)
        numero = int(input(mensaje))
    return numero

def verificar_tipo_entero(matriz: list, valor_inicial = 0) -> bool:
    """Verifica que los elementos de una matriz sean de tipo entero
    Args:
        matriz (list): Matriz en la que se buscarán los datos
        valor_inicial (int, optional): Valor base de los datos de la matriz. Defaults to 0.
    Returns:
        bool: True si la verificación salió bien, False en caso contrario
    """
    bandera = True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if type(matriz[i][j]) != int and type(matriz[i][j]) != valor_inicial:
                bandera = False
                break
    
    return bandera

def calcular_recaudacion_por_linea(matriz_recaudaciones: list) -> list:
    """Suma los elementos por cada fila individual de la matriz
    Args:
        matriz (list): Matriz utilizada para recorrer las filas
    Returns:
        list: Devuelve una lista con el cálculo
    """
    recaudacion_linea = crear_vector(len(matriz_recaudaciones))
    for i in range(len(matriz_recaudaciones)):
        suma = 0
        for j in range(len(matriz_recaudaciones[i])):
            suma += matriz_recaudaciones[i][j]
        recaudacion_linea[i] = suma
    return recaudacion_linea

#falta la funcion crear vector

def calcular_recaudacion_por_coche(matriz: list, coche: int) -> int:
    """Suma los elementos de una columna específica de la matriz
    Args:
        matriz (list): Matriz utilizada para recorrer la columna
        coche (int): numero de la columna a sumar
    Returns:
        int: Devuelve la suma de la columna especificada
    """
    if verificar_tipo_entero(matriz) and 0 <= coche < len(matriz[0]):
        total_coche = 0
        for i in range(len(matriz)):
            total_coche += matriz[i][coche]
        return total_coche
    return 0

def calcular_recaudacion_total(matriz: list) -> int:
    """Suma los datos de todos los elementos de la matriz
    Args:
        matriz (list): Matriz de donde se sacarán los valores
    Returns:
        int: La suma total
    """
    suma_total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            suma_total += matriz[i][j]
    return suma_total
