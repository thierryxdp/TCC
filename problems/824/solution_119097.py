def uppCons(frase):
    for i in range(len(frase)):
        if frase[i] == "a" or "e" or "i" or "o" or "u":
            frase = frase[i].upper()
        return frase