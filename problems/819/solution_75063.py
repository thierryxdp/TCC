def filtraMultiplos(lista,n):
    """retrona uma lista de multiplos de n de acordo com  a lista de números dada.list,float->list"""
    a=lista[-1]
    divisiveis=lista[:]
    if a%n!=0:
           list.remove(divisiveis,a)
    while len(lista)!=0:
        del lista[-1]
        
        return divisiveis