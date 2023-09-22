def conta_numero(numero, matriz):
    """função que recebe um numero inteiro e uma matriz e
    retorna quantas vezes esse número aparece na matriz.
    int, list -> int"""

    qtd = 0

    for linha in matriz:
        for aij in linha:
            if aij == numero:
                qtd += 1
    return qtd