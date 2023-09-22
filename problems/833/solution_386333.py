def conta_numero(nummero,matriz):
    '''funcao que dado um numero e uma matriz qualquer, retorna a quantidade de aparicoes do numero na matriz;
    int|float -> list'''
    aparicoes=0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if numero in matriz[i][j]:
                aparicoes=aparicoes+1
    return aparicoes