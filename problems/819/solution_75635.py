def filtra_multiplos(lista,n):
    '''funcao que a partir de uma lista e um numero n, retorna uma lista contendo todos os numeros da lista original, que forem divisiveis por n. list -> list'''
    multiplos= []
    proximo= 0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            multiplos= multiplos+[lista[proximo]]
            proximo = proximo + 1
            return multiplos