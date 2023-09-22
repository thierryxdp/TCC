def acima_da_media(lista_notas):
    media=sum(lista_notas)/len(lista_notas)
    list.append(lista_notas,media)
    posicao_media=lista_notas.index(media)
    return lista_notas(posicao_media+1)