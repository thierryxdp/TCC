def filtra_multiplos(lista,n):
    ''' funcao que dada uma lista, retorna uma lista com todos os elementos da lista original que forem divisíveis por n.
    list > list'''
    lista = []
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]%n == 0:
            divisíveis = divisíveis + (n[proximo],)
        proximo = proximo + 1
    return divisíveis