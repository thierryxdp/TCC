def melhor_volta(matriz):
    '''Função que recebe como uma entrada uma matriz e retorna uma tupla informando de quem foi
    a melhor volta da prova, com qual tempo e em que volta; list->tuple'''
    tempomin = []
    for l in matriz:
        tm = min(l)
    	list.append(tempomin,tm)
    x = min(tempomin)
    corredor = list.index(tempomin,x) + 1
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if x == matriz[l][c]:
                v = c + 1
    return (corredor,x,v)