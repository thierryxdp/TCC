def conta_numero(numero,matriz):
    '''dado um número, conta e retorna quantas vezes aquele número aparece na matriz'''
    contador = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == numero:
            contador = contador + 1
    return contador