def maiores(lista,n):
    lista2=[n]
    lista2=lista+lista2
    lista2.sort()
    return [lista2.index(n)+1:]