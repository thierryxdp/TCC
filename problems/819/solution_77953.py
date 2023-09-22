def filtraMultiplos(lista,n):
    """retorna uma lista contendo tos os elemetos da lista original que forem divisíveis por n.
    list,int->list"""
    divisiveis=()
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%2==0:
            divisiveis+=(divisiveis[proximo],)
        proximo=proximo+1
    
    return pares