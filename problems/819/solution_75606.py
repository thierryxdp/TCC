def filtraMultiplos(lista,n):
    ''' Função que retorna todos os números de uma lista,
    divisíveis por n; list, int -> list'''
    multi = []
    i = 0
    while i <len(lista):
        if lista[i]%n == 0:
            multi = multi + [lista[i]]
        i = i + 1
    return multi