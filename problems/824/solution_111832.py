def uppCons(frase):
    """comentário"""
    i = 0
    frase_cons = frase.split()
    while i < len(frase_cons):
        if "bcdfghijklmnpqrstvxwyz" in frase_cons:
            frase_cons[i] = frase_cons[i].upper()
        "".join(frase_cons)    
        i += 1
    return frase_cons