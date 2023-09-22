def filtraMultiplos(lista, n):
    """Filtra os múltiplos de um número n, retornando uma lista
com todos os elementos divisíveis por n;
list, int -> list"""
    multiplos = []
    proximo = 0
    
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            multiplos = multiplos + [lista[proximo],]
        proximo = proximo +1
    return multiplos