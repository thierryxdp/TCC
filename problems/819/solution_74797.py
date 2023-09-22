def filtraMultiplos(lista, n):
    '''filtra os múltiplos de um número n, dada uma lista
    list, int ->list'''
    i =0
    multiplos =[]
    
    while i<len(lista):
        if lista[i]%n ==0:
            multiplos =multiplos +[lista[i]]
        i =i+1
    return multiplos