conta_numero(numero, matriz):
    """recebe um numero inteiro e uma matriz, retornando quantas vezes esse numero inteiro
    aparece na matriz.
    int, lista(lista)->int"""
    cont=0
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in linha:
        cont= cont + 1
    return cont