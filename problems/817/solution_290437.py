def acima_da_media(lista_notas):
    a=sum(lista_notas)//len(lista_notas)
    lista_notas.sort()
    return lista_notas[a:]