def busca(setor, matriz):
    s = setor
    l = []
    i = 0
    for i in range(len(matriz)):
        if s == matriz[i][2]:
            m = matriz[i]
            r = m.remove(setor)
            list.append(l, r)
    return l