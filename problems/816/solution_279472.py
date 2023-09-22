def maiores(lista,n):
    """funcao calcula e retirno uma lista original(lista) com seus elementos maiores que um numero inteiro(n).
    int,int-->int"""
    lista.index(n)
    lista.append(n)
    lista.sort()
    return lista[lista.index(n)+1:]