def filtraMultiplos(lista,numero):
    """função que filtra os múltiplos de um número n de uma lista, e retorna outra lista com os elementos divisíveis por n;
       list, int -> list"""
    divisiveis = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%numero == 0:
            divisiveis = divisiveis + (lista[proximo])
        proximo = proximo + 1
    return divisiveis