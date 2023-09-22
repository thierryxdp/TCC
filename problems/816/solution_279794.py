def maiores (lista, termo):
    list.extend (lista, [termo])
    lista_nova = list.sort(lista)
    lista_certa = lista_nova[1:]
    return lista_certa