def filtraMultiplos(lista,n):
    ''' função que dada uma lista de números e um número n, retorna uma lista
    contendo todos os números da lista original que forem divisíveis por n. list -> list'''
    multiplos = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            multiplos = multiplos + [lista[proximo]]
        proximo = proximo + 1
    return multiplos