def conta_numero(numero, matriz):
    '''Retorna quantas vezes o numero inteiro inserido aparece na matriz
    fornecida;
    int, len -> int'''
    vezes=0
    for i in len(matriz):
        for j in i:
            if j==numero:
                vezes=vezes+1
    return vezes