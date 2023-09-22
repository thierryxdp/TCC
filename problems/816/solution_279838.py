def maiores(lista, n):
    """recebe uma lista e um numero n e retorna outra lista com todos
    os numeros da lista original maiores que n, list e int ->list"""
    
    list.extende(lista,[n])
    list.sort(lista)
    lista1=list.index(lista,n)
    return lista[(lista1+1):1000]