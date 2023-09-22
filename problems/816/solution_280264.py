listaMaiores = []

def maiores(lista,n):
    lista.append(n)
    lista.sort()
    p = lista.index(n)
    l = lista[p+1:]
    l.append(lista[-1])
    return lista