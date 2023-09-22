def filtraMultiplos(lista, n):
    '''funcao filtra numeros multiplos de um numero "n" dado
    e uma lista dada "lista" de numeros inteiros.
    '''
    multiplos = []
    c = 0
    while c < len(lista):
        #print(lista[c])
        if lista[c] % n == 0:
            #print(lista[c])
            multiplos.append(lista[c])
        c += 1
    return multiplos