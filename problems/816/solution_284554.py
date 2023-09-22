def maiores(lista_num, n):
    """funçao que dada uma lista e um numero n retorna uma
    lista com elementos acima de n; list, int->list"""
    list.append(lista_num,n)
    list.sort(lista_num)
    index=list.index(lista_num,n)
    return lista_num[n:]