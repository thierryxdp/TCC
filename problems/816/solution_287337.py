def maiores (lista, n):
    """retorna os números maior que n contidos na lista em ordem crescente. lista, int->lista"""
    if n in lista:
        list.sort(lista)
        return lista[list.index(lista, n)+1:]
    else:
        list.append(lista,n) 
        list.sort(lista)
        return lista[list.index(lista ,n)+1:]