def maiores(lista_int,n):
    lista_numero1=lista_int+[n]
    list.sort(lista_numero1)
    x=lista_numero1.index(n)
    maior=lista_numero1[x+1:]
    return maior