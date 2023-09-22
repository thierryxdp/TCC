def melhor_volta(matriz):
    '''dado uma matriz com os tempos em segundos dos corredores em
    cada volta, retorna uma tulpa informando de quem foi a melhor
    volta.
    list->tuple'''
    minimos=[]
    for linha in matriz:
        minimos=minimos+[min(linha)]
    menor_tempo=min(minimos)
    corredor=list.index(minimos,menor_tempo)
    volta=list.index(matriz[corredor],menor_tempo)
    
    return (corredor+1,menor_tempo,volta+1)