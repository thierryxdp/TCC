def uppCons(frase):
    """
    """
    nova_frase = frase
    for i in frase:
        if i not in "aeiou":
            nova_frase = nova_frase.replace(nova_frase[i],frase)
        return nova_frase