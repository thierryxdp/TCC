def maiores(lista,n):
    lista.append(n)
    lista.sort()
    p = lista.index(n)
    listaMaiores = lista[p+1:]
    return listaMaiores

def acima_da_media(L):
    x = (sum(L)/len(L))
    listaAcima = maiores(L,x)
    return listaAcima