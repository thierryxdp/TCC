def busca(s,matriz):
    c=0
    d=[]
    while c< len(matriz):
        if matriz[c][2] == s:
            lista=matriz[c].remove(s)
            d.append(lista)
            c=c+1
        else:
            c=c+1
    return d