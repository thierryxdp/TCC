def melhor_volta(matriz):
    '''função que dada uma matriz'''
    lista_min = []
    volta = 1
    for i in matriz:
        corredor = 1
        for j in matriz[volta - 1]:
            lista_min += [matriz[volta - 1][corredor - 1]]
            corredor += 1
        volta += 1
    melhor_tempo = min(lista_min)
    melhor_corredor = list.index(min(matriz), melhor_tempo)
    melhor_volta = list.index(matriz,melhor_corredor)
    return melhor_corredor, melhor_tempo, melhor_volta