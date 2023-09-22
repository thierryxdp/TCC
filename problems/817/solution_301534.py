def maiores(lista,n):
    lista.append(n)
    lista.sort()
    i=lista.index(n)
    return lista[i+1:]
def acima(lista):
    return maiores(lista,5)