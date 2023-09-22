def acima_da_media(lista_notas):
    a=sum(lista_notas)//len(lista_notas)
    b=lista_notas.index(a)
    list.sort(lista_notas)
    return lista_notas[b:]