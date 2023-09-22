def melhor volta(matriz):
    '''função que dada uma matriz'''
    volta = 1
    for i in matriz:
        corredor = 1
        for j in matriz[volta]:
            if matriz[volta][corredor] == min(min(matriz)):
                return corredor, matriz[volta][corredor], volta