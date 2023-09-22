def filtraMultiplos(l,n):
    '''Essa função filtrar os múltiplos de um número n, dado o valor de entrada uma lista de números e um número'''
    ''' list,int -> list'''
    l2 = []
    proximo = 0
    while proximo < len(l):
        if l [proximo]%n == 0:
            l2 = l2 + [l[proximo]]
        proximo = proximo + 1
    return l2