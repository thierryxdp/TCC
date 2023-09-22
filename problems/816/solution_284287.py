def maiores(Lista,n):
    """Função que retorna uma lista ordenada em ordem crescente os números maiores 
    que n, dado como parâmetros de entrada a lista e o numero n.
    list,float=>list"""
    
    list.insert(Lista,0,n)
    list.sort(Lista)
    lugar = list.index(Lista,n)
    listaF = Lista[lugar+1:]
    return listaF