def conta_numero(n, matriz):
    '''Conta quantas vezes um número inteiro aparece em uma matriz;
       int, list -> int'''
    contador = 0
    for linha in matriz:
        for aij in linha:
            if aij == n:
                contador += 1
    return contador