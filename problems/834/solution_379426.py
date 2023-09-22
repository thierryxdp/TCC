def numb_da_matriz(matriz):
    '''função que dada uma matriz calcula a quantidade de elementos da matriz; matriz>>int'''
    l= len(matriz)
    c= len(matriz[0])
    return c*l

def soma(matriz):
    soma= 0
    for l in matriz:
        for c in l:
            soma= soma + c
    return soma

def media_matriz(matriz):
    return round((soma(matriz)/numb_da_matriz(matriz)), 2)