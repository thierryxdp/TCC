def melhor_volta(matriz):
    '''recebe uma matriz informando o tempo de cada
    corredor durante as 10 voltas feitas e retorna quem foi
    o melhor da prova em qual tempo e em qual volta t list->tuple'''
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