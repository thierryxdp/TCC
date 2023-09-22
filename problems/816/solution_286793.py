def maiores(lista_numeros,n):
    l1=lista_numeros+[n]
    list.sort(l1)
    a=list.index(l1,n)
    return l1[a+1:]