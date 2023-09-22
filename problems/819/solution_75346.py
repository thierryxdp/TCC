def filtraMultiplos(lista,n):
    '''A função calcula e retorna uma lista contendo todos os elementos(números) divisíveis por n
    list,int->list'''
    multiplos = []
    proximo = 0
    while proximo<len(lista):
        if lista[proximo]%n == 0:
            multiplos = multiplos + [lista[proximo]]
        proximo = proximo + 1
    return multiplos