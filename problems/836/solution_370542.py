def busca(s,m):
    lista = []
    for i in m:
        if s.lower() in i[2].lower() :
            del i[2]
            lista.append(i)
    return lista