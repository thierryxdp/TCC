def conta_numero(numero, matriz):
    '''uma função que dado um número inteiro e uma matriz qualquer, conta e retorna quantas vezes
    aquele número aparece na matriz
    int, lista -> int'''
    quantidade = 0
    for a in matriz:
        for b in a:
            if b == numero:
                quantidade += 1
    return quantidade