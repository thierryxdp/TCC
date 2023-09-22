def filtraMultiplos(numeros,n):
    """A função retorna os multiplos de uma lista dada como 
    entrada e de um numero n
    list, int--->list"""
    multiplos = []
    dividendo = 0
    while dividendo < len(numeros):
        dividendo = dividendo+1
        if (numeros[dividendo] % n) == 0:
            list.append(multiplos, numeros[dividendo])
    return multiplos