def maiores(lista,n):
    lista1=lista+[n]
    lista2=list.sort(lista)
    lista3=list.index(lista2,0)
    return lista2 - lista3