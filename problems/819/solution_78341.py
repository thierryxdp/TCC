def filtraMultiplos(lista, n):
    """Dada uma lista com números aleatorios e um numero n, cria uma 
    nova lista somente com os numeros multiplos de n. list -> list """
    div = ()
    prox = 0
    while prox <len(lista):
        
        if lista[prox]%n == 0:
            div = div + (lista[prox])
        prox = prox + 1
    return div