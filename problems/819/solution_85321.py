def filtraMultiplos(numeros,n):
    '''Recebe uma lista de números e um número n e retorna todos aqueles
     que forem divisíveis por n.(list,int -> list)'''
    divisiveis = []
    proximo = 0
    while proximo < len(numeros):
        if numeros[proximo]%n == 0:
            divisiveis = divisiveis + [numeros[proximo],]
        proximo = proximo + 1
    return divisiveis