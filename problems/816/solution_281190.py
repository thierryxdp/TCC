def maiores(lista,n):
    lista.append(n)
    lista.sort()
    x=lista.find(n)
    return lista[x+1:]