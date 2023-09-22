def filtraMultiplos(lista,n):
    '''funcao que dada uma lista e um numero n,retornará a uma lista que contem todos
    os numeros da lista original que forem divisíveis por n,
    list ->list'''
    multiplos = []
    proximo = 0
    while proximo < len(lista):
        if m[proximo]%n == 0:
            multiplos = multiplos + [lista[proximo]]
        proximo = proximo + 1
    return multiplos