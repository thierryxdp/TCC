def melhor_volta(matriz):
    '''
    Recebe como entrada uma matriz 6x10 e retorna 
    uma tupla contendo: o corredor com a melhor volta,
    qual tempo e em que volta.
    
    list(list) -> tuple(int)
    '''
    lista = []
    lista2 = []
    for i in matriz:
        tempo = min(i)
        volta = i.index(tempo)
        lista.append(tempo)
        lista2.append(volta)
    menor = min(lista)
    corredor = lista.index(menor)
    volta2 = lista2.index[corredor]
    return (corredor, menor, volta2)