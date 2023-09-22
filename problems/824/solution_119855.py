def uppCons(frase):
    """
    """
    frase1 = frase
    for i in frase:
        if i in "aeiou":
            frase1 = frase1.replace(frase[i], frase1.upper())
            return frase1