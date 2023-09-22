listaMaiores = []

def maiores(lista,n):
    lista.append(n)
    lista.sort()
    p = lista.index(n)
    return lista[p+1:-1]