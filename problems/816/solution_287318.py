def maiores(l, n):
    c = 0
    lista = []
    while c<len(l):
        if l[c]>n:
    		lista = [l[c]] + lista
    		c = c + 1
    list.sort(lista)
    return c