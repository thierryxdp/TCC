def uppCons (frase):
    """" """
    consoantes="bcdfghjklmnpqrstvwxyz"
    while frase in "bcdfghjklmnpqrstvwxyz":
        frase=consoantes.upper().join(frase)
    return frase