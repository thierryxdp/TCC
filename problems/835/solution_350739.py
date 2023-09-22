def melhor_volta(matriz):
    '''função que retorna uma tupla com o corredor que apresentou a melhor volta,o melhor tempo e a 
    respectiva volta, dada como parâmetro uma matriz com os tempos de cada volta.
    list --> tuple'''
    minimos = []
    for linha in matriz:
        minimos = minimos+[min(linha)]
    menor_tempo = min(minimos)
    corredor = list.index(minimos,menor_tempo)
    volta = list.index(matriz[corredor],menor_tempo)
    
    return (corredor+1,menor_tempo,volta+1)