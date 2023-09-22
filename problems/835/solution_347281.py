def melhor_volta(matriz):
    '''função que dada uma matriz'''
    lista_min = []
    for i in matriz:
            list.append(lista_min, min(i))
    melhor_tempo = min(lista_min)
    melhor_corredor = list.index(lista_min, melhor_tempo)
    melhor_volta = list.index(matriz[melhor_corredor], melhor_tempo) + 1
    return melhor_corredor, melhor_tempo, melhor_volta