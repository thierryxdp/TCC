def busca(s, m):
    l = [i for i in m if s in i]
    for c in l:
        c.pop(2)
    return l