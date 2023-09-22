def insere(x,y):
    list.append(x,y)
    return sorted(x)

def maiores(x,y):
    w=insere(x,y)
    z=w.index(y)
    return w[z:]