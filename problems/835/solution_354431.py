def melhor_volta(m):
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