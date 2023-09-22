def maiores(lista,n):
    """Função que retorna uma lista ordenada com numeros maiores 
    que n, dado como parâmetros a lista e o numero 'n'
    list,float=>list"""
    list.insert(lista,0,n)
    list.sort(lista)
    lugar = list.index(lista,n)
    listaF = lista[lugar+1:]
    return listaF