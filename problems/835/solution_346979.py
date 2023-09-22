def melhor_volta(matriz):
    ''' idéia: pegar a matriz 6x10,
supor que o valor minimo esta na posição m[o][o],
caso nao esteja, fazer o contador andar por toda matriz
achando o menor, assim que achar o menor de todos
ela vai substituir no valor minimo.'''
    
    corredor = len(matriz)
    volta = len(matriz[0])
    minimo = matriz[0][0]
    tupla = ()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]<minimo:
                minimo = matriz[i][j]
            if minimo == matriz[i][j]:
                if corredor in matriz[i]:
                    corredor = i
                    volta = 9
                tupla = (corredor,minimo,volta)
    return tupla