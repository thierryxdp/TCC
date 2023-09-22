def maiores(lista,n):
    """retorna outra lista com os números maiores que n"""
    list.append(lista,n)         #insere o elemento n na lista
    list.sort(lista)             #
    posicao = list.index(lista,n)
    del lista [:posicao+1]
    return lista