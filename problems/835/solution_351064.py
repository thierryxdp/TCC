def melhor_volta(matriz):
    '''funcao que, dada uma matriz 6x10, retorna uma tupla, informando o dono da melhor volta, o tempo e em qual volta;
    list -> tuple'''
    melhores_voltas=()
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            melhores_voltas=melhores_voltas+(matriz[i][j]))
    
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if min(melhores_voltas)==matriz[i][j]:
                return (i,min(melhores_voltas),j)