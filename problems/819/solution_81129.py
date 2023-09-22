def filtraMultiplos(multiplos,n):
    '''funçao que dada uma lista vazia e um numero n,retorna uma lista contendo todos os numeros divisiveis por n da lista original; lista',int -> lista'''
    multiplos = []
    indice = 0
    while indice < len(multiplos):
        if multiplos[indice]%n == 0 :
            multiplos = multiplos + multiplos[indice]
            indice = indice + 1
    return multiplos