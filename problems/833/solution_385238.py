def conta_numero(numero, matriz):
    '''dado um numero inteiro e uma matriz de numeros inteiros
    de tamanho qualquer, retorna quantas vezes aquele numero
    aparece na matriz.
    int, list -> int'''
    vezes = 0
    for linha in matriz:
        for n in linha:
            if n == numero:
                vezes = vezes + 1
    return vezes