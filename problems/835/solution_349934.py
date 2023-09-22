def melhor_volta(matriz):
    '''função que retorna uma tupla dizendo quem fez a
    melhor volta, com qual tempo e em qual volta'''
    minimos=[]
    for linha in matriz:
        minimos=minimos+[min(linha)]
    menor_tempo=min(minimos)
    corredor=list.index(minimos,menor_tempo)
    volta=list.index(matriz[corredor],menor_tempo)
    
    return (corredor+1,menor_tempo,volta+1)