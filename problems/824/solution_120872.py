def uppCons (frase):
    frase.upper()
    frase = list(frase)
    i = 1
    for i in range(len(frase)):
        if frase[i] in "aeiou":
            frase[i] = frase[i].lower()
    frase = "".join(frase)
    return frase