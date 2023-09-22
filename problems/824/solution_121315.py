def uppCons(frase):
    """Função que recebe uma frase e retorna a frase com as consoantes maiúsculas. str -> str"""
    frase = list(frase)
    for f in range(len(frase)):
        if frase[i] in "BCDFGHJKLMNPQRSTVWXYZÇbcdfghjklmnpqrstvwxyzç":
            frase[i] = frase[i].upper()
    frase = "".join(frase)
    return frase