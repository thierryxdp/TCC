def uppCons(frase):
    """coment"""
    i=0
    while i<len(frase):
        if frase[i] in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
            str.upper(frase[i])
        i=i+1
    return frase