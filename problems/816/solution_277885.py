def maiores(lista,n):
    """calculo e retorno de uma lista que contenha todos os numeros da lista original maiores que n"""
    a=lista
    b=lista.append(n)
    b=list.sort(a)
    c=a[n:]
    return c