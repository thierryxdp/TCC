def melhor_volta(matriz):
    '''Retorna uma tupla informando: De quem foi a melhor volta 
    da prova, com qual tempo e em que volta. Dada uma matriz 
    6 x 10 contendo os tempos em segundos dos corredores em cada
    volta
    list -> tuple '''
    minimos=[]
    for linha in matriz:
        minimos=minimos+[min(linha)]
    menor_tempo=min(minimos)
    corredor=list.index(minimos,menor_tempo)
    volta=list.index(matriz[corredor],menor_tempo)
    
    return (corredor+1,menor_tempo,volta+1)