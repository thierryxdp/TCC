def uppCons(frase):
    """Esta função recebe uma string e torna as consoantes maiusculas
    str -> str"""
    frase = list(frase)
    for i in range(len(frase)):
        if frase[i] in "BCDFGHJKLMNPQRSTVWXYZÇbcdfghjklmnpqrstvwxyzç":
            frase[i] = frase[i].upper()
    frase = "".join(frase)
    return frase