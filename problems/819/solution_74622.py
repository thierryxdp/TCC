def filtraMultiplos(lista, n):
    '''funcao que retorna apenas os numeros da lista inserida que forem multiplos de n em uma nova lista
    int, list -> list'''
    multiplos = []
    i = 0
    while i < len(lista):
        if lista[i]%n == 0:
           multiplos = multiplos + [lista[i]]
        i = i + 1
    return multiplos