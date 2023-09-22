def acima_da_media(lista_notas):
    soma=sum(lista_notas)
    n_d=len(lista_notas)
    media=int(soma/n_d)
    list.append(lista_notas,media)
    posicao_media=lista_notas.index(media)
    return lista_notas[posicao_media+1:]