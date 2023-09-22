def maiores(lista, num):
    lista.append(num)
    if max(lista) == num:
        return []
    sorted_lista = sorted(lista)
    index_num = sorted_lista.index(num)
    sorted_lista.remove(num)
    return sorted_lista[index_num+1:]