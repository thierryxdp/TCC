def acima_da_media(lista_numero):
    n=((sum(lista_numero))/len(lista_numero))
    list.append(lista_numero, n)
    list.sort(lista_numero)
    a=list.index(lista_numero,n)
    return lista_numero[a+2:]