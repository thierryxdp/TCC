def filtraMultiplos (numeros,n):
    '''Função que retorna os elementos de uma lista(números)
    divisiveis por n.
    list,int->list'''
    cont = 1
    while numeros % n ==0:
        cont = cont + 1
        numeros = numeros + 1
    return cont