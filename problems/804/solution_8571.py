def filtra_pares(tupla):
    """A função receberá uma tupla com quatro valores inteiros, e
    retornará uma nova tupla apenas com os valores inteiros pares da
    tupla original. Todos os valores pares deverão estar na mesma ordem
    em que estavam.
    Entrada: Tuple(Int, Int, Int, Int)
    Saída: Tuple(Int, Int, Int, Int)"""

    a,b,c,d = tupla
    tuplapar = tuple()
    
    if (a%2) == 0:
        tuplapar = tuplapar + (a,)
    if (b%2) == 0:
        tuplapar = tuplapar + (b,)
    if (c%2) == 0:
        tuplapar = tuplapar + (c,)
    if (d%2) == 0:
        tuplapar = tuplapar + (d,)
    return tuplapar