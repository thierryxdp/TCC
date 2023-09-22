def maiores(lista,n):
    """essa função recebe uma lista e um número n e retorna
    uma nova lista contendo apenas os números da lista original 
    maiores que n;
    list,int-->list"""
    list.append(lista,n)
    lista = sorted(lista)
    x = list.index(lista,n)
    y = x + 1
    return lista[y:]