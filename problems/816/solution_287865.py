def maiores(l,n):
    """dada uma lista de numeros inteiros e um numero n, retorna outra lista
    que contem todos os numeros da original maiores que n, ordenados em ordem
    crescente. list->list"""
    list.append(l,n)
    list.sort(l)
    f=list.index(l,n) 
    return l[f+1:]