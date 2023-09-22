def busca(s, m):
    return [i.remove(i[2]) for i in m if s in i]