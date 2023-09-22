def filtraMultiplos(lista,n):
    """função que filtra múltiplos de um número n. função que recebe
    uma lista e retorna uma nova lista que é divisores de n. list,int->list"""
    multiplos=()
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            multiplos=multiplos+(lista[proximo],)
        proximo= proximo+1
    return multiplos