def maiores(l, n):
    c = 0
    lista = []
    while l[c]>n:
        lista = l[c] + lista
        c = c + 1
        list.sort(lista)
        if c>len(l):
            return lista
    else:
        return []