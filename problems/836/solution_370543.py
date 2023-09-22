def busca(s,m):
    lista = []
    for i in m:
        if s in i[2] :
            del i[2]
            lista.append(i)
    return lista