def uppCons (frase):
    """
    """
    frase1 = frase
    for i in frase:
        if i in "aeiou":
            frase1 = frase.replace(i,i.upper())
            return frase1