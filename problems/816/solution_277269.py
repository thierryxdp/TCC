def maiores(lista,n):
    """Função que retorna uma nova lista contendo apenas os números da lista 
    original maiores que n. list[int],int->list"""
    a1 = list.index(lista,n)
    if n in lista:
        list.sort(lista)
        return lista[a1+1]
    if n not in lista:
        list.append(lista,n)
        list.sort(lista)
        return lista[a1+1]