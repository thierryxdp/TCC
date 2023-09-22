def filtraMultiplos(lista,n):
    '''
    funçao que recebe uma lista de numeros e um numero n
    e retorna outra lista contendo todos os elementos da 
    lista original que forem divisiveis por n
    list, int -> list
    '''
    multiplos = []
    x = 0
    while x < len(lista):
        if lista[x] % n == 0:
            multiplos = multiplos + [lista[x]]
        x = x + 1
    return multiplos