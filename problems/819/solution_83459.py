def filtraMultiplos(lista,n):
    multiplos = []
    proximo = 0
    while proximo<len(lista):
        if proximo/n==int:
            multiplos = proximo + multiplos
        proximo = proximo + 1
    return multiplos