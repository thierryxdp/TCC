def uppCons(frase):
    """comentário"""
    i = 0
    while i < len(frase):
        if "bcdfghijklmnpqrstvxwyz" in frase:
            frase[i].upper()
        i += 1
    return frase