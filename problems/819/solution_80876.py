def filtraMultiplos(num,n):
    '''Recebe uma lista de numeros(num) e um numero n, retorna uma lista 
    com os numeros divisiveis por n.
    list, int --> list'''
    result = []
    i = 0
    while i < len(num):
        if numeros[i]%n == 0:
            list.append(result, num[i])
        i = i+1
    return result