def melhor_volta(matriz):
    '''Função que retorna, dado uma matriz com com os 
tempos em segundos dos corredores em cada volta
, retornaquem foi a melhor volta da prova, com qual tempo 
e em que volta. ;list->tuple'''
    minimos=[]
    for linha in matriz:
        minimos=minimos+[min(linha)]
    menor_tempo=min(minimos)
    corredor=list.index(minimos,menor_tempo)
    volta=list.index(matriz[corredor],menor_tempo)
    
    return (corredor+1,menor_tempo,volta+1)