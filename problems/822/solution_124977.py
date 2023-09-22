def repetidos(lista):
    '''Dada uma lista de números, retorna o número de vezes que um
    elemento da lista é igual ao anterior.
    list -> int'''
    cont = 0
    acumul = 0
    while cont < len(lista):
        if lista[cont] == lista[cont+1]:
            acumul = acumul + 1
        cont = cont + 1
    return acumul