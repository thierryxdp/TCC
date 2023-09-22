def busca(s, matriz):
    r = []
    for i in matriz:
        for j in i:
            if j == s:
                r.append(i)
    return r