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
    return min(lista_min)