def maiores(lista,n):
    """funcao que recebe uma lista de num inteiros(lista) e um 
    numero inteiro(n) e retorna uma nova lista com os numeros da 
    lista maiores que n.
    list,int->list"""
    a = lista + [n]
    list.sort(a)
    c = list.index(a,n)
    return a[c+1:]