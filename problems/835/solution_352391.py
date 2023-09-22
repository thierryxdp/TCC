def melhor_volta(matriz):
    '''funcao que, dada uma matriz 6x10, retorna uma tupla, informando o dono da melhor volta, o tempo e em qual volta;
    list -> tuple'''
    melhores_voltas=[]
    for i in range(0,6):
        melhores_voltas=melhores_voltas+[min(matriz[i])]
        
    for i in range(0,6):
        for j in range(0,10):
            if min(melhores_voltas)==matriz[i][j]:
                return (i+1,min(melhores_voltas),j+1)