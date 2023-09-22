def filtraMultiplos(lista, n):
    '''Função que dado como entrada uma lista de números e um número "n",
    retorna outra lista contento todos os elementos da lista original que
    sejam divisíveis por n.'''
    divisivel = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            divisivel = divisivel + [lista[proximo]]
        proximo = proximo + 1
    return divisivel