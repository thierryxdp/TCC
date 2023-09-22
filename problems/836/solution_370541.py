def busca(s,m):
    lista = []
    for i in m:
        if s.lower() in i[2].lower() :
            lista.append(i)
    return lista