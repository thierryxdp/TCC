def filtraMultiplos(lista:list,n:int)->int:
    """Dada uma lista e um número inteiro n, retorna uma nova lista com os múltiplos por n da lista dada como entrada."""
    multiplos=()
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            multiplos=multiplos+(lista[proximo],)
        proximo=proximo+1
        return list(multiplos)