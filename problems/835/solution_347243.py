def melhor_volta(matriz):
    '''função que dada uma matriz'''
    volta = 1
    for i in matriz:
        corredor = 1
        for j in matriz[volta - 1]:
            if matriz[volta - 1][corredor - 1] == min(min(matriz)):
                return corredor, matriz[volta - 1][corredor - 1], volta
            corredor += 1
        volta += 1