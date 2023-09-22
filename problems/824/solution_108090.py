def uppCons(frase):
    """fdgfdgg"""
    i = 0
    while i < len(frase.split):
        if "bcdfghjklmnpqrstvxwyz" or "BCDFGHJKLMNPQRSTVWXYW" in frase:
            frase = frase[i].upper
        i = i + 1
    return frase