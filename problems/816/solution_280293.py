def maiores(lista,n):
    """essa funcao calcula uma lista de numeros inteiros e um numero inteiro n, retorna outra lista, que contenha todos os numeros da lista original maiores que n; list, int -> list"""
    if n not in lista:
        list.append(lista,n)
    list.sort(lista)
    ind=list.index(lista,n)
    listaf=lista[ind+1:]
    return listaf