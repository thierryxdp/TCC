def conta_numero(numero, matriz):
    '''função que recebe um numero e uma matriz e retorna quantas o numero fornecido aparece na matriz'''
    soma = 0
    for x in range (len (matriz)):
        for y in range (len(matriz[x])):
            if numero == matriz[x][y]:
                soma = soma + 1
    return soma