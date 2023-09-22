def conta_numero(numero, matriz):
    """Retorna um inteiro que indica quantas vezes um numero
    dado como entrada aparece em uma matriz dada como entrada.
    int, lista(lista) -> int"""
    contador = 0
    for l in range(0,len(matriz)):
        for c in range(0,len(matriz[c])):
            if matriz[l][c] == numero:
                 contador += 1
    return contador