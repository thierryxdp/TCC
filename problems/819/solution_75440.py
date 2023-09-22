def filtraMultiplos(a,b):
    '''função que recebe como entrada uma lista de numeros e um numero e retorna outra lista; list->list'''
    multiplos = []
    proximo = 0
    while proximo < len(a):
        if a[proximo]%b == 0:
            multiplos = multiplos + [a[proximo]]
        proximo = proximo + 1
    return multiplos