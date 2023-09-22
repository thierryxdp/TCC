def maiores (lista, termo):
    list.extend (lista, [termo])
    list.sort(lista)
    list.pop(lista, 0)
    return lista