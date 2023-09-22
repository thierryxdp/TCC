def filtraMultiplos(lista,n):
    """Dada uma lista de numeros e um numero a parte, retorna os numeros
    dessa lista que sao multiplos de n
    Entradas:
    	lista: lista
        n: int
    Returns:
    	lista
    """
    i = 0
    numeros = []
    while i<len(lista):
        if lista[i]%n == 0:
            numeros = numeros + lista[i]
        i = i + 1
    return numeros