def busca(s, matriz):
    r = []
    for i in matriz:
        for j in i:
            if j == s:
                r.append(i)
    for i in r:
        for j in i:
            if j == s:
                i.remove(j)
    return r