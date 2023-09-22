def filtraMultiplos(lista,n):
    '''Função que ao receber uma lista de numeros, retorna uma lista contendo os multiplos do parametro n'''
    '''list, int -> list'''
    multiplos = []
    i = 0
    while i < len(lista):
        if lista[i]%n == 0:
            multiplos = multiplos + [lista[i]]
        i = i + 1
    return multiplos