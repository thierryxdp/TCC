def maiores(l, n):
    if n<l[0]:
        lista = [l[0]]
    if n<l[1]:
        lista = lista + [l[1]]
    if n<l[2]:
        lista = [l[2]]
    if n<l[3]:
        lista = lista + [l[3]]
        return lista