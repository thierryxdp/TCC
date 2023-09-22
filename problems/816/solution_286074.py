def maiores(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero)
    x=list.index(lista_numero,n)
    del lista_numero[:x+1]
    return lista_numero