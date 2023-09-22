def conta_numero(numero, matriz):
    '''dado um numero inteiro e uma matriz de inteiros de tamanho qqr, conta e
retorna qts vezes aquele numero aparece na matriz'''
    cont = 0
    for linha in matriz:
        for aij in linha:
            if aij == numero:
                return cont = cont + 1