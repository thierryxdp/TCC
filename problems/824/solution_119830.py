def uppCons (frase):
    """
    """
    frase1 = frase
    for letra in frase:
        if letra not in  frase["a","e","i","o","u"]:
            frase1 = frase1.replace(frase,frase1.upper())
    		return frase1