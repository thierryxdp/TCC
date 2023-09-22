def maiores(lista,n):
    """dada uma lista e um numero inteiro n, retorna outra
    lista que contenhas os elementos da lista original
    maiores que n;
    list[int],int->list[int]"""
    if n in lista:
        list.sort(lista)
        return lista[list.count(lista,n)+list.index(lista,n):]
    elif n not in lista:
        list.append(lista,n)
        list.sort(lista)
        return lista[list.index(lista,n)+1:]