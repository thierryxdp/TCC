def melhor_volta(matriz):
    '''Dado uma matriz 6x10, retorna uma tupla informando de quem foi a melhor prova,com qual tempo e em que volta
    list->tuple'''
    
    tempo=[]
    
    for x in range(len(matriz)):
        tempo=tempo+[min(matriz[x])]
    menor_tempo=min(tempo)     
    corredor=list.index(tempo,menor_tempo)
    volta=list.index(matriz[corredor],menor_tempo)+1
    return (corredor+1,menor_tempo,volta)