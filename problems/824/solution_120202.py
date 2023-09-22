def uppCons(frase):
    frase = list(frase)
    for i in range(len(frase)):
        if frase[i] in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
            frase[i] = frase[i].upper()
    frase = "".join(frase)
    return frase