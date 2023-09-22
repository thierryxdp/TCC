def uppCons(frase):
    for i in range(len(frase)):
        if frase[i] not in "aeiou":
            frase[i].upper()
    return frase