def busca(s,m):
    l = []
    for linha in range(len(m)):
        if s in m[linha][2]:
            a = m[linha].remove(s)
            l.append(a)
    return l