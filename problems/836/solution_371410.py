def busca(s, matriz):
    r = []
    for i in matriz:
        for j in matriz:
            if j == s:
                r.append(i)
    return r