def filtraMultiplos(l,n):
    '''recebe uma lista de números e um número n, retorna uma lista contendo os elementos da lista fornecida que forem divisíveis por n
list, int -> list'''
    divisiveis = ()
    x = 0
    while x < len(l):
        if l[x]%n == 0:
            divisiveis = divisiveis + (l[x],)
        x = x + 1
    return list(divisiveis)