def filtraMultiplos(lista, n):
    ''' A função recebe uma lista, um número 'n' e retorna os multiplos de n
        presentes na lista.
        list, int -> list'''
    multiplos = []
    proximo = 0
    while proximo <= (len(lista)-1):
        if lista[proximo]%n == 0:
            multiplos = multiplos + [lista[proximo],]
        proximo = proximo + 1
    return multiplos