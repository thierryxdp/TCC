def filtraMultiplos(lista,n):
    """Função que filtra os multiplos de um numero e retorna uma lista contendo os elementos da lista original que são divisíveis por n.
    list, int - > list"""
    multiplos = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            multiplos = multiplos + [lista[proximo],]
        proximo = proximo + 1
    return multiplos