def faltando(lista):
    list.sort(lista)
    primeiro=lista[0]
    ultimo=lista[len(lista)-1]

    n= primeiro
    faltando=0

    while n<ultimo:
        if n not in lista:
            faltando=faltando+n
        n=n+1

    if faltando>0:
        return faltando
    else:
        return lista[len(lista)-1]+1