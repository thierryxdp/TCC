def filtraMultiplos(x,y):
    """A função ira filtrar todos os numeros que sao multiplos de "y" dentro da lista.
    list + int --> list """
    r = []
    for item in x:
        if item%y == 0 :
            r = r + [item, ]
    return r