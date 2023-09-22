def conta_numero(numero, matriz):
    '''Uma função que dado um numero inteiro e uma matriz qualquer,
    conta e retorna quantas vezes aquele numero apareceu na matriz
    int, matriz -> int'''
    quantidade = 0
    for a in matriz:
        for b in a:
            if b == numero:
                quantidade += 1
    return quantidade