def uppCons(frase):
    """fdgfdgg"""
    i = 0
    while i < len(frase):
        if "bcdfghjklmnpqrstvxwyz" or "BCDFGHJKLMNPQRSTVWXYW" in frase[i]:
            frase = frase[i].upper
        i = i + 1
    return frase