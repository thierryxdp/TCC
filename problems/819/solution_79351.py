def filtraMultiplos(lista,n):
    """essa funçao recebe uma lista e um numero n e retorna uma outra lista contendo os numeros da lista original divisiveis por n"""
    """entrada: list, int"""
    """saida: list"""
    multiplos=[]
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n=0:
            multiplos=multiplos+[lista[proximo]]
        proximo=proximo+1
    return multiplos