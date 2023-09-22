def maiores(numeros, n):
    """dada uma lista de numeros int e um numero int, a funçao retorna uma
    lista com todos os numeros da lista maiores que n
    list,int->list"""
    N = numeros
    list.extend(numeros,[n])
    N.sort()
    i = list.index(N,n)
    return N[i+1:]