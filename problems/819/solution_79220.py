def filtraMultiplos(lista,n):
    """
    	Dada uma lista, retorna uma lista contendo os elementos da lista inicial que são divisíveis por n
        list,int -> list
    """
    lista_divis=[]
    l=0
    while l<len(lista):
        if lista[l]%n == 0:
            lista_divis += [lista[l]]
        l += 1
    return lista_divis