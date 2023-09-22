def maiores (lista,n ):
    """dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n, ordenados em ordem crescente.
    
    entrada->lista 
    retorna ->lista
    """
    
    list.sort (lista)
    
    if lista [0]> n:
        return lista
    elif lista [1]>n:
        return lista [1:]
    elif lista [2]>n:
        return lista [2:]
    elif lista [3]>n:
        return lista  [3:]