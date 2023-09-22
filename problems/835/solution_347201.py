def melhor_volta(matriz):
    '''Funcao que recebe como entrada uma matriz 6x10 com os tempos (segundos) dos corredores em cada volta.
    E retorna uma tupla contendo: corredor com a melhor volta, em qual tempo e qual volta.
    list -> tuple'''
    
    listaMelhoresT = []
    voltas = []
    
    for i in matriz:
        melhorT = min(i)
        list.append(melhorT, listaMelhoresT)
        volta = list.index(i, melhorT)
        list.append(volta, voltas)
        
    
    melhorT = min(listaMelhoresT)
    corredor = list.index(listaMelhoresT, melhorT)
    melhorVolta = voltas[corredor]
    
    return (corredor + 1, melhorT, melhorVolta + 1)