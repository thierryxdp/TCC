def filtraMultiplos(lista,numero):
    '''dikadnakdna'''
    multiplos = []
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]%numero == 0:
            multiplos.append(lista[proximo])
            proximo = proximo + 1
            return multiplos