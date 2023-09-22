def uppCons(frase):
    """Retorne a frase com todas as suas consoantes minúsculas"""
    i = 0
    nova_frase = ''
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVXYZbcdfghjklmnpqrstvxyz':
            nova_frase.append(str.upper(frase[i]))
        i = i + 1
    return nova_frase