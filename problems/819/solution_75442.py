def filtraMultiplos(r,n):
    '''funcao que dada uma lista e um numero n,retornará a uma lista que contem todos
    os numeros da lista original que forem divisíveis por n,
    list ->list'''
    multiplos = []
    proximo = 0
    while proximo < len(r):
        if m[proximo]%n == 0:
            multiplos = multiplos + [r[proximo]]
        proximo = proximo + 1
    return multiplos