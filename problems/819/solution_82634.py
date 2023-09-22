def filtraMultiplos(lista,n):
    ''' funcao que recebe uam lista e um numero e retorna uam lista com os multiplos do numero; list, int: list'''
    
    pares = []
    i = 0
    while i <len(lista):
        if lista[i]%n == 0:
            pares = pares + [lista[i],]
        i = i + 1
    return pares