def conta_numero(numero,matriz):
    '''Função que retorna a quantidade de vezes que um número aparece em uma matriz, dado o número e a matriz;int,list->int'''
    apareceu=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                apareceu=apareceu+1
    return apareceu