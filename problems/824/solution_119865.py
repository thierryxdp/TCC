def uppCons(frase):
    """
    """
    frase1 = frase
    for i in frase:
        if i in not ("aeiou"):
            frase1 = frase1.replace(frase,frase1.upper())
            return frase1