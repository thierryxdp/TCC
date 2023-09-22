def maiores(lista_numeros, n):
    a= list.sort(lista_numeros)
    b= list.index(lista_numeros,n)
    c= lista_numeros[(b+1):]
    d= list.count(c,n)
    e= c[(0+d):]
    return e