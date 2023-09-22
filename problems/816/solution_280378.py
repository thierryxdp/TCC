def maiores(lista,n):
    """Retorna uma lista que contém todos os elementos da lista, que é o primeiro parâmetro, que são maiores que n, que é o segundo parâmetro;
    list,int->list"""
    a=lista+[n]
    b=a.sort()
    c=list.index(b,n)
    return b[:c]