def uppCons(frase):
    """
    """
    frase1 = frase
    for i in frase:
        if i in range(len("aeiou")):
            frase1 = frase1.replace(i,frase1.upper())
            return frase1