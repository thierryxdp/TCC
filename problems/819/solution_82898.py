def filtraMultiplos(lista,n):
    '''Função que recebe lista e retorna com números múltiplos
    do número n. list, int-->list'''
    multiplos = []
    i = 0
    
    while i < len(lista):
        if lista[i] % n == 0:
            multiplos.insert(i, lista[i])
        i += 1 
            
    return multiplos