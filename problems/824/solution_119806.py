def uppCons (frase):
    """
    """
    frase1 = frase
    for i in frase:
        if i not in "aeiou":
            frase1 = frase.replace(i,frase1.upper())
            return frase1