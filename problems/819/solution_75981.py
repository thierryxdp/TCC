def filtraMultiplos(numeros,n):
    '''funçao que dada uma lista com numeros e um numero n retorna
    todos os multiplos do numero n presentes na lista'''
    multiplos = []
    indice = 0
    while indice < len(numeros):
        if numeros[indice] % n == 0:
            multiplos.append(numeros[indice])
        indice = indice + 1
    return multiplos