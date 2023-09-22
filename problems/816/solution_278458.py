def maiores(lista_numero,n):
    """funcao que dado uma lista de numeros inteiros e um numero n, retorma outra lista que contenha todos os numeros da lista original maiores que n.
    list, int ->"""
    lista= lista_numero+[n]
    lista.sort(lista)
    x=list.index(lista,n)
    y= list.count(lista,n)
    return lista[a+b:]