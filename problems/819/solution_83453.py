def filtraMultiplos(lista_num, n):
    multiplos = []
    proximo = 0
    while proximo < len(lista_num):
        if lista_num[proximo]%n==0:
            multiplos =  multiplos + [lista_num[proximo]]
        proximo = proximo + 1
    return multiplos