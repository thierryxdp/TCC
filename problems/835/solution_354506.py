def melhor_volta(matriz):
    '''funçao que recebe como uma entrada uma matriz e retorna uma tupla informando de quem foi
    a melhor volta da prova, com qual tempo e em que volta; list->tuple'''
    tempo = []
    for l in matriz:
        y = min(l)
    list.append(tempo,y)
    x = min(tempo)
    corredor = list.index(tempo,x) + 1
    for f in range(len(matriz)):
        for z in range(len(matriz[f])):
            if x == matriz[f][z]:
                v = z + 1
    return (corredor,x,v)