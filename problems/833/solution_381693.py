def conta_numero(numero,matriz):
    ''' Dado um numero e uma matriz (de qualquer tamanho) de inteiros, a funcao
    diz quantas vezes o numero dado aparece na matriz;
    int, list -> ints '''
    
    vezes = 0
    nLinhas = len(matriz)
    nColunas = len(matriz[0])
    
    if matriz == []:
        return 0
    
    else:
        for i in range(nLinhas): 
            for j in range(nColunas):
                if matriz[i][j] == numero:
                    vezes += 1
                
    return vezes