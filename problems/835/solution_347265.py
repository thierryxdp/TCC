def melhor_volta(matriz):
    '''função que dada uma matriz'''
    lista_min = []
    volta = 1
    for i in matriz:
        corredor = 1
        for j in matriz[volta - 1]:
            list.append(lista_min, [matriz[volta - 1][corredor - 1]])
            if min(matriz[volta - 1]) == min(min(matriz)):
                melhor_volta = volta
            corredor += 1
        volta += 1
    melhor_tempo = min(lista_min)
    melhor_corredor = list.index(matriz, matriz[melhor_volta])
    return melhor_corredor, melhor_tempo, melhor_volta