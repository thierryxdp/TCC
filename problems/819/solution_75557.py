def filtraMultiplos(lista,n):
    """calculo e retorno de uma funcao que retorna multiplos de um numero de uma lista."""
    multiplos=()
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            multiplos=multiplos+(lista[proximo],)
        proximo=proximo+1
    return multiplos