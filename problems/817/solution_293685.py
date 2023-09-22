def acima_da_media(lista_notas):
    s = sum(lista_notas)
    l = len(lista_notas)
    n = s / l
    list.sort(lista_notas)
    a = list.index(lista_notas,n)
    return lista_notas[a+1:]