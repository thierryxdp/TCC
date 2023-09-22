def uppCons(frase):
    """coment"""
    consoantes="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    for letter in frase:
        if letter in consoantes:
            letter.upper()
    return frase