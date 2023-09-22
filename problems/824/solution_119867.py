def uppCons(frase):
    """
    """
    frase1 = frase
    for i in frase:
        if i not in ("aeiou"):
            frase1.upper()
            frase1 = frase1.lower(i)
            return frase1