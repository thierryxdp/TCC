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
    elif len(lista)>2 and lista [2]>n:
        return lista [2:]
    elif len (lista)>3 and lista [3]>n:
        return lista  [3:]
    elif len (lista)>4 and lista  [4]>n:
        return lista[4:]
    elif len (lista)>5 and lista  [5]>n:
        return lista [5:]
    elif len (lista)>6 and lista [6]>n:
        return lista[6:]
    elif len (lista)>7 and lista  [7]>7:
        return lista [7:]
    elif len (lista)>8 and lista [8]>8:
        return lista [8:]
    elif len (lista)>9 and lista [9]>9:
        return lista [10:]
    else:
        return []