def maiores(lista,n):
    '''funçao que dada uma lista de numeros inteiros e um numero n retorna outra
    lista com os numeros da lista original maiores que n'''
    list.sort(lista)
    return lista[lista:n]