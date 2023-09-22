def uppCons(frase):
    """
    """
    frase1 = frase
    for i in frase:
        if i in range(len("aeiou")):
            frase1.upper() = frase1.replace(i,i.lower())
            return frase1