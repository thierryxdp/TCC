def maiores (lista, n):
    """retorna os números maior que n contidos na lista em ordem crescente. lista, int->lista"""
    if n in lista:
        return [(list.index(list.sort(lista), n)+1)]
    else:
         return [(list.index(list.sort(list.append(lista,n))))+1]