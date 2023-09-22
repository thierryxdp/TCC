if n not in lista:
        list.append(lista,media)
    list.sort(lista)
    ind= list.index(lista,media)
    lista1= lista[ind+1:]
    return lista1