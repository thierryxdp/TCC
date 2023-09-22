def filtraMultiplos(l,n):
    '''A função recebe uma lista de numeros e um numero n e retorna outra lista com 
    os elementos da lista original que são multiplos de n'''
    multiplos = []
    proximo = 0
    while proximo <len(l):
        if l[proximo]/n == l[proximo]//n:
            multiplos = multiplos + [l[proximo],]
        proximo = proximo + 1
    return multiplos