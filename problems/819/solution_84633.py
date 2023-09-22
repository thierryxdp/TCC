def filtraMultiplos(lista, n):
    """Essa função informa quais elementos da lista são divisíveis por n
    lista, int -> lista"""
    i = 0
    multiplos = ()
    while i<len(lista):
        i i+1
        if lista[i]%n == 0:
            multiplos = multiplos + (lista[i],)
    return multiplos