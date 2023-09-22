def filtraMultiplos(numeros,n):
    '''funçao que dada uma lista vazia e um numero n,retorna uma lista contendo todos os numeros divisiveis por n da lista original; lista',int -> lista'''
    numeros = []
    indice = 0
    while indice < len(numeros):
        if numeros[indice]%n == 0 :
            numeros = numeros + numeros[indice]
            indice = indice + 1
    return numeros