def melhor_volta(m):
    '''funçao que recebe uma matriz com o tempo dos corredores
    em cada volta e retorna uma tupla informando a melhor volta; list ->tuple''' 
    tmin=[]
    for u in m:
        tm=min(u)
        list.append(tmin,tm)
    x= min(tmin)
    corredor=list.index(tmin,x) + 1
    for u in range(len(m)):
        for c in range(len(m[1])):
            if x == m[u][c]:
                v = c+1
    return (corredor,x,v)