def filtraMultiplos(lista,numero):
    """ função que filtra os múltiplos de um número n e retorna outra lista contendo os elementos da lista original que são divisíveis por n;
        lista,int -> lista"""
    divisiveis = []
    proximo = 0
    while proximo < len(lista):
        if t[proximo]%numero == 0:
            divisiveis = divisiveis + (lista[proximo],)
        proximo = proximo + 1
    return divisiveis