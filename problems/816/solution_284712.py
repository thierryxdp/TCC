def maiores(lista,n):
    """
    dada uma lista de números inteiros e um número 'n', retorna
    outra lista que contenha todos os números maiores que 'n' da
    lista original.
    """
    
    list.append(lista,n)
    list.sort(lista)
    x=list.index(lista,n)
    lista2=lista[x+1:]
    return lista2