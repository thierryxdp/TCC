def filtraMultiplos(lista,n):
    """funcao que filtra os multiplos de um numero n, list, int->int"""
    multiplos=[]
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            multiplos=multiplos+[lista[proximo],]
        proximo=proximo+1
    return multiplos