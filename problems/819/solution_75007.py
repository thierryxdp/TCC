def filtraMultiplos(m,n):
    '''função que dado uma lista de números e um outro número chamado de n, retorna uma nova lista contendo os elementos da lista original que forem divisíveis por n'''
    multiplos = []
    proximo = 0
    while proximo < len(m):
        if m[proximo]%n == 0:
            multiplos = multiplos + [m[proximo],]
        proximo = proximo + 1
    return multiplos