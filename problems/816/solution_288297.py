def maiores(lista,n):
    list.sort(lista)
    if n in lista:
        x=n+1
        c=lista[x:]
        return c