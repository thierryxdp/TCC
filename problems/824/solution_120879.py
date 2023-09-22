def uppCons (frase):
    frase.upper()
    frase = list(frase)
    for i in range(1,len(frase)):
        if frase[i] in "aeiou":
            frase[i] = frase[i].upper()
    frase = "".join(frase)
    return frase