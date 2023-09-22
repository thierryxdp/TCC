def melhor_volta(matriz):
    """Função que dada uma matriz de uma corrida, retorna o corredor mais rápido, o melhor tempo ea melhor volta.
    list --> tuple"""
    
    corredores = 0
    tempo = 1000
    voltas = 0
    
    for lista in range(len(matriz)):
        if min(matriz[lista]) < tempo:
            tempo = min(matriz[lista])
            corredores = lista + 1
            voltas = list.index(matriz[lista], min(matriz[lista])) + 1
            
    return (corredores, tempo, voltas)