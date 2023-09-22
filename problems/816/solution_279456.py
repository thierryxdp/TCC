def maiores(lista,n):
    """retorna uma lista que contenha os numeros da lista original maiores que n
    list,int -> list"""
    
    lista.append(n)
    lista.sort()
    lista.index(n)
    
    indice_lista = lista.index(n)
    
    return lista[indice_lista+1:0]