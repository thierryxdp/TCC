def filtraMultiplos(lista, n):
    
    """Calcula e retorna uma lista contendo os múltiplos de um número n, a partir de uma lista dada
    Entradas: Lista escolhida(lista) e número(n)
    list,int --> list"""

    multiplos = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%(n) == 0:
            multiplos = multiplos + [lista[proximo],]
        proximo = proximo + 1
    return multiplos