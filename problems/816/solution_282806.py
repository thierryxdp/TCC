def maiores (lista,n ):
    """dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n, ordenados em ordem crescente.
    
    entrada->lista 
    retorna ->lista
    """
    
    list.sort (lista)
    
    if lista [0]> n:
        return lista
    elif len(lista)>1 and lista [1]>n:
        return lista [1:]
    elif lista [2]>n:
        return lista [2:]
    elif lista [3]>n:
        return lista  [3:]
    elif lista  [4]>n:
        return lista[4:]
    elif lista  [5]>n:
        return lista [5:]
    elif lista [6]>n:
        return lista[6:]
    elif lista  [7]:
        return lista [7:]
    elif lista [8]:
        return lista [8:]
    elif lista [9]:
        return lista [9:]
    else:
        return []