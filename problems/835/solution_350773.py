def melhor_volta(matriz):
    '''Recebe uma matriz com os resultados de uma corrida de kart e retorna
    quem teve a melhor volta, o tempo da melhor volta e qual volta foi
    list->tuple'''
    minimos=[]
    for linha in matriz:
        minimos=minimos+[min(linha)]
    menor_tempo=min(minimos)
    corredor=list.index(minimos,menor_tempo)
    volta=list.index(matriz[corredor],menor_tempo)
    return (corredor+1,menor_tempo,volta+1)