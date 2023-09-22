def melhor_volta(matriz):
    '''retorna, a partir da matriz 6x10, uma tupla com quem fez
    a melhor volta, o tempo e qual foi a volta
    list->tuple'''
    minTempos=[]
    for sublista in matriz:
        minTempos=minTempos+[min(sublista)]
    indicec=list.index(minTempos,min(minTempos))
    corredor=indicec+1
    indicev=list.index(matriz[indicec],min(matriz[indicec]))
    volta=indicev+1
    return(corredor,min(minTempos),volta)