def filtraMultiplos(numeros,n):
    '''funçao que dada uma lista de numeros e um numero n retorna 
    os multiplos de n na lista'''
    multiplos = []
    indice = 0
    while indice < len(numeros):
        if numeros[indice]%n == 0:
            multiplos.append(numeros[indice])
            indice = indice + 1
        else:
            pass
    return multiplos