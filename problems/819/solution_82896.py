def filtraMultiplos(lista,n):
    '''Função que recebe lista e retorna com números múltiplos
    do número n. list, int-->list'''
    multiplos = []
    contador = 0
    
    while contador < len(lista):
        if lista[contador] % n == 0:
            multiplos.insert(contador, lista[contador])
            contador = contador + 1
   
    return multiplos