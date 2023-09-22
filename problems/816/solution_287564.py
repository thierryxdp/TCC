def maiores(lista,n):
    """Retorna os valores maiores que n de uma lista de numeros;lista,int=>lista"""
    list.sort(lista)
    print (lista)
    indice = lista.index(n)
    
    return lista[indice+1:]