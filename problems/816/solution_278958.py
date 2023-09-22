def maiores(lista, n):
    """função que retorna uma lista somente com os elementos maiores que n.
    
    list,int -> list
    
    exemplo:
    maiores([1,2,4],3)==[4]
    """
    lista.append(n)
    lista.sort()
    lista=lista[lista.index(n)+1:]
    
    return lista