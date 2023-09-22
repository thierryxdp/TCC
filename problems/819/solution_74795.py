def filtraMultiplos(lista, n):
    """Função que dada uma lista e um número n, retorna uma nova lista contendo
os elementos da lista original que são múltiplos de n.
    list, int -> list"""
    listanova = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            listanova = listanova + [lista[proximo]]
        proximo = proximo + 1
    return listanova