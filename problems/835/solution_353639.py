def melhor_volta(matriz):
    '''Esta função recebe como entrada uma matriz 6x10, com os tempos em segundos dos corredores de 10 voltas, e retorna uma tupla informando de quem foi a melhor volta, com qual tempo e em que volta.
list->tuple'''
    lista=[]
    for i in range(len(matriz)):
        list.append(lista,min(matriz[i]))
        for j in range(len(matriz[i])):
            corredor= list.index(lista,min(lista))+1
            melhor_volta=min(lista)
            volta=list.index(matriz[corredor-1],melhor_volta)
    return (corredor,melhor_volta,volta)