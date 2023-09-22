def acima_da_media(lista_notas):
    media=sum(lista_notas)/len(lista_notas)
    list.append(lista_notas,media)
    list.sort(lista_notas)
    return lista_notas[list.index(lista_notas,n)+1:]