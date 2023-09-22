def filtraMultiplos(lista,n):
    """Dado uma lista e um número, retorna os números da lista divisiveis pelo numero. list,int>list"""
    i = 0
    listaf = []
    while i<len(lista):
        if lista[i]%n == 0:
            listaf += lista[i]
    	i += 1
    return listaf