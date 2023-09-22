def melhor_volta(matriz):
    '''Dado uma matriz 6x10 contendo os tempos de cada corredores em cada volta,
retorna a melhor volta da prova, com seu tempo e em que volta.
list-->tupla'''
    minimos=[]
    for linha in matriz:
        minimos=minimos+[min(linha)]
    menor_tempo=min(minimos)
    corredor=list.index(minimos,menor_tempo)
    volta=list.index(matriz[corredor],menor_tempo)
    
    return (corredor+1,menor_tempo,volta+1)