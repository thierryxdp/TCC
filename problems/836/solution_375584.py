def busca(s,matriz):
    c=0
    d=[]
    while c< len(matriz):
        if matriz[c][2] == s:
            lista=[matriz[c][0],matriz[c][1],matriz[c][3]]
            d.append(lista)
            c=c+1
        else:
            c=c+1
    return d