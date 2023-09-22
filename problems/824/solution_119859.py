def uppCons(frase):
    """
    """
    frase1 = frase
    for i in frase:
        if i in range(len("aeiou")):
            frase1 = frase1.upper.replace(i,i.lower())
            return frase1