def maiores(lista,n):
    """Dada uma lista e um inteiro retorna outra lista que contenha todos os números
       da lista original maiores do que n.
       list int -> list"""
    
    list.append(lista,n)
    list.sort(lista)
    x = list.index(lista,n)
    
    return lista[x-1:]