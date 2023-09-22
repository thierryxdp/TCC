def maiores (lista,n):
    """dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n, ordenados em ordem crescente.
    
    entrada->list, int
    retorna->list"""
    
    list.sort (lista)
    list.remove (lista,n-1)
    list.remove (lista,n-2)
    
    
    return lista