def maiores(lista,n):
    """retorna a parada la"""
    
    lista.append(n)
    lista.sort(n)
    lista.index(n)
    
    indice_lista = lista.index(n)
    
    return lista[indice+1:0]