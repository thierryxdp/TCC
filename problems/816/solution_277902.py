def maiores(lista,n):
    """calculo e retorno de uma lista que contenha todos os numeros da lista original maiores que n"""
    a=lista
    b=a.append(n)
    d=list.sort(a)
    e=list.index(a,n)
    c=a[e:]
    return c