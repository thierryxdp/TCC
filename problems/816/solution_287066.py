def maiores(lista,n):
    """retorna uma lista que contém todos os números originais maiores que n, ordenados em ordem crescente
    list,int->list"""
    
    lista.sort()
    lista.append(n)
    for x in lista:
       if x<n:
        lista.remove(x) 
    
    return lista