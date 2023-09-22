def melhor_volta(m):
    '''funçao que recebe como uma entrada uma matriz e retorna uma tupla informando de quem foi
    a melhor volta da prova, com qual tempo e em que volta; list->tuple'''
    tempomin = []
    for l in m:
        tm = min(l)
    list.append(tempomin,tm)
    x = min(tempomin)
    corredor = list.index(tempomin,x) + 1
    for l in range(len(m)):
        for c in range(len(m[l])):
            if x == m[l][c]:
                v = c + 1
    return (corredor,x,v)