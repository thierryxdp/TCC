def melhor_volta(matriz):
    '''recebe uma matriz com 6 corredores e 10 voltas deles e retorna uma
    tupla com o corredor com a volta mais rapida, qual o tempo e em qual
    volta
    list->tuple'''
    listaMenores: []
    for i in matriz:
        list.append(listaMenores,min(i))
    Corredor = list.index(listaMenores,min(listaMenores))
    
    Volta = list.index(matriz[Corredor],min(matriz[Corredor]))
    
    return Corredor+1,min(matriz[Corredor]),Volta+1