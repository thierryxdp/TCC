listaMaiores = []

def maiores(lista,n):
    lista.sort()
    lista.append(n)
    return lista[n+1:-1]