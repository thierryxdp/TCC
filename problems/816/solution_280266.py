listaMaiores = []

def maiores(lista,n):
    lista.append(n)
    lista.sort()
    p = lista.index(n)
    l = lista[p+1:]
    
    return l