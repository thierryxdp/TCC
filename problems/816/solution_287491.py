def maiores(lista_numero, n):
    a= list.sort(lista_numero)
    b= list.index(lista_numero,n)
    c= lista_numeros[(b+1):]
    d= list.count(c,n)
    e= c[(0+d):]
    return e