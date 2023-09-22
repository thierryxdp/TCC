def filtraMultiplos(l,n):
    '''Retorne outra lista contendo todos
    os elementos da lista original que forem
    divisíveis por n. list, int -> list'''
    original = []
    proximo = 0
    while proximo < len(l):
        if l[proximo]%n == 0:
           original = original + [l[proximo]]
        proximo = proximo + 1
    return original