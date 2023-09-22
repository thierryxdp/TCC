def melhor_volta(matriz):
    '''recebe uma matriz de devolve um tuple com seu
    menor valor e seus índices
    list -> tuple'''
    
    k = 0
    lista = []
    for lin in matriz:
        k = min(lin)
        lista.append(k)
    
    tempo = min(lista)
    corredor = lista.index(tempo)
    num_volta = matriz[corredor].index(tempo)
    
    return (corredor + 1, tempo, num_volta + 1)