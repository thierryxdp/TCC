def maiores(lista,n):
    "Retorne dada lista com valores ordenados maiores que n;lista,int->lista"
    lista.append(n)
    lista.sort()
    x=lista.index(n)
    return lista[x:]