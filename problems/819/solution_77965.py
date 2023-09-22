def filtraMultiplos(lista,n):
    """função que recebe uma lista de números e um número n 
    e retorna uma nova lista apenas com os números que são
    múltiplos de n.
    list, float -> list"""
    multiplos = []
    proximo = 0
    
    while proximo < len(lista):
        if lista[proximo] % n == 0:
            multiplos = multiplos + [lista[proximo]]
        proximo = proximo + 1
    return multiplos