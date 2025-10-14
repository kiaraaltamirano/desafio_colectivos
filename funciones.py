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

def validar_rango(numero: int|float, inicio: int|float, fin: int|float) -> bool:
    """Valida un número dentro del rango deseado
    Args:
        numero (int|float): Número a validar
        inicio (int|float): Inicio del rango
        fin (int|float): Final del rango
    Returns:
        bool: True si el número es validado efectivamente, False en caso contrario
    """
    bandera = False
    if numero >= inicio and numero <= fin:
        resultado = True
    return bandera

def ingresar_numero_entero(mensaje: str, mensaje_error: str, inicio: int, fin: int, reintentos: int) -> int|None:
    """Pide un número entero por terminal
    Args:
        mensaje (str): Mensaje que se mostrará al usuario
        mensaje_error (str): Mensaje en caso de tener que reingresar el número
        inicio (int): Inicio del rango en el que debe estar el número
        fin (int): Fin del rango
        reintentos (int): Número de reintentos para reingresar el número
    Returns:
        int|None: Devuelve int en caso de que la validación haya salido bien, None en caso contrario
    """
    numero = int(input(mensaje))
    if type(numero) == int:
        if validar_rango(numero,inicio,fin):
            numero_validado = numero
        else:
            numero_validado = None
            print(f"{mensaje_error}, le quedan {reintentos} reintentos")
            if reintentos > 0:
                numero_validado = ingresar_numero_entero(mensaje, mensaje_error, inicio, fin, reintentos - 1)

    return numero_validado

def ingresar_numero_flotante(mensaje: str, mensaje_error: str, inicio: float, fin: float, reintentos: float) -> float|None:
    """Pide un número entero por terminal
    Args:
        mensaje (str): Mensaje que se mostrará al usuario
        mensaje_error (str): Mensaje en caso de tener que reingresar el número
        inicio (float): Inicio del rango en el que debe estar el número
        fin (float): Fin del rango
        reintentos (float): Número de reintentos para reingresar el número
    Returns:
        float|None: Devuelve float en caso de que la validación haya salido bien, None en caso contrario
    """
    numero = float(input(mensaje))
    if type(numero) == float:
        if validar_rango(numero,inicio,fin):
            numero_validado = numero
        else:
            numero_validado = None
            print(f"{mensaje_error}, le quedan {reintentos} reintentos")
            if reintentos > 0:
                numero_validado = ingresar_numero_entero(mensaje, mensaje_error, inicio, fin, reintentos - 1)

    return numero_validado

def cargar_recaudacion(matriz: list):
        linea = ingresar_numero_entero("Ingrese el número de línea: ","Error, reingrese el número",1,3,2)
        coche = ingresar_numero_entero("Ingrese el número de coche: ","Error, reingrese el número",1,5,2)
        recaudacion = ingresar_numero_flotante("Ingrese el monto de recaudación: ","Error, reingrese el monto",1,100,2)
        matriz[linea-1][coche-1] += recaudacion

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

def crear_vector(size: int, value: any):
    """Crea un vector
    Args:
        size (int): Longitud del vector
        value (any): Valor inicial de los datos de la lista
    Returns:
        _type_: Devuelve la lista creada
    """
    lista = [value] * size
    return lista

def calcular_recaudacion_por_linea(matriz: list) -> list:
    """Suma los elementos por cada fila individual de la matriz
    Args:
        matriz (list): Matriz utilizada para recorrer las filas
    Returns:
        list: Devuelve una lista con el cálculo
    """
    recaudacion_linea = crear_vector(len(matriz),0)
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
        recaudacion_linea[i] = suma
    return recaudacion_linea

def calcular_recaudacion_por_coche(matriz: list, columna: int) -> list:
    """Suma los elementos por cada columna individual de la matriz
    Args:
        matriz (list): Matriz utilizada para recorrer las columnas
        columna (int): Columna elegida para calcular
    Returns:
        int: Devuelve la suma de la columna especificada
    """
    total = 0
    for i in range(len(matriz)):
        total += matriz[i][columna-1]
    return total

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
