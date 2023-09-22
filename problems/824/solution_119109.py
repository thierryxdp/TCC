def uppCons(frase):
    """
    """
    nova_frase = frase
    for i in frase:
        if i not in "aeiou":
            nova_frase = nova_frase.replace(frase, nova_frase)
        return nova_frase