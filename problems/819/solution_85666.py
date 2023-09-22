def filtraMultiplos(lista, numero):
    """filtra os multiplos de um numero. list, float -> list"""
    i=0
    divisiveis=[]
    for i in lista:
        while i%numero==0:
            list.append(divisiveis,i)
            i=i+1
    return divisiveis