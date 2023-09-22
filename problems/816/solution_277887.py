def maiores(lista,n):
    """calculo e retorno de uma lista que contenha todos os numeros da lista original maiores que n"""
    a=lista
    b=list.sort(a)
    d=a.append(n)
    c=a[n:]
    return c