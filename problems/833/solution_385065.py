def conta_numero(numero,matriz):
    """..."""
    matriz = []
    contador = 0
    for i in range(len(matriz)):
        if numero in matriz:
            list.count(matriz,numero)
            contador = contador + 1
    return contador