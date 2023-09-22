def filtraMultiplos(lista,n):
    """Função que recebe uma lista e um numero n e retorna uma lista
    contendo os numeros da lista que são divisiveis por n""" 
    i = 0
    r = []
    while i < len(lista):
        if lista[i]%n == 0:
            r = r + [lista[i]]
            i = i + 1
        else:
            i = i + 1
    return r