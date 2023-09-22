def uppCons(frase):
    """comentário"""
    i = 0
    frase = split.frase()
    while i < len(frase):
        if "bcdfghijklmnpqrstvxwyz" in frase:
            frase[i].upper()
            "".join(frase)
        i += 1
    return frase