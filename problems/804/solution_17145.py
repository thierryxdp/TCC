def filtra_pares(t):
    """Tem como objetivo receber uma tupla e retornar 
    apenas seus elementos pares.
    tupla > tupla"""#Start your python function here
    pares = tuple(())
    for valor in t:
        if valor%2==0:
            pares.append(valor)
    return pares