def filtraMultiplos (lista,n):
    """função que dada uma lista e um número n, retorna todas os números da lista original que
são divisíveis por n"""
    x=len(lista)
    proximo=0
    divisivel=()
    while proximo<x:
        if lista[proximo]%n==0:
            divisivel=divisivel+ (lista[proximo],)
        proximo=proximo+1
    return divisivel