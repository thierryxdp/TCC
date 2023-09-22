def conta_numero(numero,matriz):
    """Retorna quantas vezes um numero dado por parametro aparece em uma matriz;
    list -> int"""
    i = 0
    contador = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[i]):
            if matriz[i][j] == numero:
                contador += 1
            j += 1
        i += 1
    return contador