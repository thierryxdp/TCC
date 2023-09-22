def uppCons(frase):
    """Retorne a frase com todas as suas consoantes minúsculas"""
    i = 0
    nova_frase = frase
    while frase:
        if frase[i] in 'BCDFGHJKLMNPQRSTVXYZbcdfghjklmnpqrstvxyz':
            frase = str.upper(frase[i])
        i = i + 1
        return frase