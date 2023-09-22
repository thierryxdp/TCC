def conta_numero(numero, matriz):
    '''dado um numero inteiro e uma matriz de inteiros de tamanho qqr, conta e
retorna qts vezes aquele numero aparece na matriz'''
    cont = 0
    numeros = str(numero)
    for n in numeros:
        if n == matriz:
            cont = cont + 1
    return cont