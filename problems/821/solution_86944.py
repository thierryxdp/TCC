def fatorial(n):
    """Fornece o cálculo do fatorial de N"""
    contador = 0
    listanum = list(range(1,n+1))
    fatorial = 1
    while contador < len(listanum):
        fatorial = fatorial*listanum[contador]
        contador+= 1
    return fatorial