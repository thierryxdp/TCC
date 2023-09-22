def uppCons(frase):
    """
    Essa função transforma as consoantes minisculas para maisculas de uma frase.
    Entrada = str
    Saída = str
    """

    i = 0
    f2 = []
    while i < len(frase):
        if frase[i] in "bcdfghjklmnpqrstvxywzç":
            list.append(f2, str.upper(frase[i]))
        else:
            list.append(f2, frase[i])
        i = i + 1
    return str.join("", f2)