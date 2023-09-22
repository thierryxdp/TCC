def uppCons(frase):
    """
    """
    frase1 = frase
    for i in frase:
        if i not in "aâeiouAEIOU ":
          frase1 = frase1.replace(i,i.upper())
    return frase1