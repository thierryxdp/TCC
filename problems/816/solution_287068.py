def maiores(lista,n):
    """retorna uma lista que contém todos os números originais maiores que n, ordenados em ordem crescente
    list,int->list"""
   
    lista.append(n)
    lista.sort()
    lista.index(n)
    del lista[0: lista.index(n)]
    
    return lista