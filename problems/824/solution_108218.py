def uppCons (frase):
    """" """
    i=0
    consoantes="bcdfghjklmnpqrstvwxyz"
    while frase[i] in consoantes:
        frase=consoantes.upper()
        i=i+1
    return frase