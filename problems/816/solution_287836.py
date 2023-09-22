def maiores(lista_numero,n):
    lista_numero.append(n)
    list.sort(lista_numero)
    x=lista_numero.index(n)
    del(lista_numero[:x+1])
    return lista_numero