def maiores(lista,n):
    """funcao calcula e retirno uma lista original(lista) com seus elementos maiores que um numero inteiro(n).
    int,int-->int"""
    lista.index(n)
    lista.append(n)
    lista.sort()
    ind=lista.index(n)
    return lista[ind+1:]