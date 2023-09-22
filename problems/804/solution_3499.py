def filtra_pares(e1,e2,e3,e4):
    """..."""

    lis = [e1,e2,e3,e4]
    lisnova = [i for i in lis if i%2 == 0]

    return tuple(lisnova)