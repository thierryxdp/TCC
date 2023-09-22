def melhor_volta(matriz):
    '''Dada uma matriz 6 x 10 com os tempos em segundos dos corredores em cada volta, retorna qual corredor fez a melhor volta, em qual tempo e em qual volta'''
    '''list->tuple(int,float,int)'''
    tempo=min(matriz[0])
    volta=list.index(matriz[0],min(matriz[0]))+1
    corredor=1
    for i in range(1,len(matriz)):
        if min(matriz[i])<(tempo):
            tempo=min(matriz[i])
            volta=list.index(matriz[i],min(matriz[i]))+1
            corredor=i+1
    return (corredor,tempo,volta)