def melhor_volta(matriz):
    '''analisando o conjunto de tempos de corredores de Kart em 10 voltas,
    retorna uma tupla com quem teve a melhor volta, seu respectivo tempo e 
    em que volta;
    list->tuple'''
    minimos=[]
    for linha in matriz:
        minimos=minimos+[min(linha)]
    menor_tempo=min(minimos)
    corredor=index(minimos,min(minimos)
    volta=index(matriz[corredor],menor_tempo)
    
    return (corredor,menor_tempo,volta)