ef melhor_volta(matriz):
    '''Retorna uma tupla dizendo quem foi a melhor volta o tempo e em que volta dado um dos 6 corredores'''
    minimos=[]
    for linha in matriz:
        minimos=minimos+[min(linha)]
    menor_tempo=min(minimos)
    corredor=list.index(minimos,menor_tempo)
    volta=list.index(matriz[corredor],menor_tempo)
    
    return (corredor+1,menor_tempo,volta+1)