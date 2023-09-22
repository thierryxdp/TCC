def filtraMultiplos(numeros, n):
    '''Função que recebe uma lista de números e um número n
    e verifica quais números da lista são multiplos de n e 
    retorna uma lista com esses números.
    [list], int -> [list]'''
    multiplos = []
    i = 0
    while i < len(numeros):
        if numeros[i]%n == 0:
            multiplos = multiplos + [numeros[i]]
		i = i + 1
    return multiplos