def filtraMultiplos(lista, n):
    '''função que retorna uma lista de números múltiplos de um número n, a partir de uma lista de números dada; list, int -> list'''
    
    divisores = ()
    i = 0
    while i < len(lista):
        if lista[i]%n == 0:
            divisores = divisores+(lista[i])
        i = i+1
    return list(divisores)