def maiores (lista, termo):
    list.extend (lista, [termo])
    list.sort(lista)
    list.pop(lista, 1)
    return lista