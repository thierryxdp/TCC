def maiores(numeros, n):
    '''Dado uma lista de numeros e um numero n, retorna outra lista com os numeros maiores que n.
    list, int -> list'''
    numeros.append(n)
    numeros.sort()
    pos = numeros.index(n)
    numeros.pop(pos)
    maiores = numeros[pos:]
    return maiores