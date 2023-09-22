def conta_numero(numero,matriz):
    '''Função que dado um número, retorna quantas vezes o mesmo
    se encontra presente em uma matriz; int, list -> int'''
    quant = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero == matriz[i][j]:
                quant = quant + 1
    return quant