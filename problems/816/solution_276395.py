def maiores (lista, n):
    """ funcao ira receber uma lista de numeros inteiros e u numero n, e assi ira retornar uma nova lista que contenha todos os numeros da lista original que sejam maiores que n
    list, int -> list"""
    list.append (lista,n)
    list.sort (lista)
    return lista [ list.index (lista,n) + 1 : ]