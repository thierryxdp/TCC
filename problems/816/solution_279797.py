def maiores (lista, termo):
    list.extend (lista, [termo])
    lista_nova = list.sort(lista)
    return lista_nova[1:]