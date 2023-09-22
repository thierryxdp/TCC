def filtraMultiplos(lista,n):
    """Essa função informa quais números de uma lista são divisíveis por n
    lista, int -> lista"""
    i = 0
    multiplos = ()
    while i<len(lista):
        if lista[i]%n == 0:
            multiplos = multiplos + (lista[i],)
        i = i+1
    return multiplos