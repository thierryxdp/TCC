def busca(x,y):
    '''Busca, dado um setor x, os funcionários na matriz Y.
    str, list -> list'''
    lista=[]
    for i in range (len(y)):
        if x==y[i][2]:
            list.append(lista,y[i])
            del(y[i][2])
    return lista