def conta_numero(numero,matriz):
    '''Dada uma matriz de inteiros e um número retorna o numero de aparições deste número
    list,int -> int'''
    aparicoes = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                aparicoes += 1
    return aparicoes