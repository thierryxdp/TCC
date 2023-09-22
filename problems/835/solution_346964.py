def melhor_volta(matriz):
    ''' idéia: pegar a matriz 6x10,
supor que o valor minimo esta na posição m[o][o],
caso nao esteja, fazer o contador andar por toda matriz
achando o menor, assim que achar o menor de todos
ela vai substituir no valor minimo.'''
    
    corredor = 6
    volta = 10
    minimo = matriz[0][0]
    
    for i in range(0,6):
        
        for j in range(0,10):
            tupla = (matriz[i],matriz[0][0],matriz[j])
            if matriz[i][j]<minimo:
                minimo = matriz[i][j]
            tupla = (corredor,minimo,volta)
    return tupla