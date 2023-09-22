def filtraMultiplos(lista,n):
    '''Dada uma lista de números e um número, retorna outra lista
    contendo todos da lista originaç divisiveis por n.
    list, int -> list'''
    acumul = []
    cont = 0
    while cont < len(lista):
        if lista[cont]//n == 0:
            acumul = acumul+lista[cont:cont+1]
        cont = cont +1
    return acumul