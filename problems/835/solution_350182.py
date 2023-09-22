def melhor_volta(matriz):
    '''dada uma matriz 6 x 10 com os tempos em segundos dos 
    corredores em cada volta, retorna uma tupla informando quem 
    fez a melhor volta, com qual tempo e em que volta
    list->tuple'''
    
    melhor=[]
    for linha in matriz:
        melhor=melhor+[min(linha)]
    menor_tempo=min(melhor)
    corredor=list.index(melhor,menor_tempo)
    volta=list.index(matriz[corredor],menor_tempo)
    
    return (corredor+1,menor_tempo,volta+1)