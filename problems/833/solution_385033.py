def conta_numero(numero:int,matriz:list)->int:
    '''Função que retorna quantas vezes o número aparece na matriz'''
    ind=0
    for i in range(len(matriz)):
           for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                   ind=ind+1
    return ind