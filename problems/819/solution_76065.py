def filtraMultiplos(lista,n):
    """
    Filtra os multiplos de n que estao na lista
    """
    i=0
    multiplos=[]
    while i<len(lista):
            if lista[i]%n==0:
                list.append(multiplos,lista[i])
            i=i+1
    return multiplos