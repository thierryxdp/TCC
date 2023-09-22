def maiores(lista,n):
    """Retorna uma outra lista contendo somente os
    números da lista de entrada maiores que n;
    list, int-> list"""
    list.sort(lista)
    posicao_n= list.index(lista,n)
    new_list= lista[posicao_n+1:]
    return new_list