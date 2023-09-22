def melhor_volta(m):
    '''funçao que recebe uma matriz com o tempo dos corredores
    em cada volta e retorna uma tupla informando a melhor volta; list ->tuple''' 
    tmin = []
    for l in m:
        tm = min(l)
    list.append(tmin,tm)
    x = min(tmin)
    corredor = list.index(tmin,x) + 1
    for l in range(len(m)):
        for c in range(len(m[l])):
            if x == m[l][c]:
                v = c + 1
    return (corredor,x,v)