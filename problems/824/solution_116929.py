def uppCons(frase):
    """Retorne a frase com todas as suas consoantes minúsculas"""
    i = 0
    qtd_consoantes = ''
    while frase:
        if frase[i] in 'BCDFGHJKLMNPQRSTVXYZbcdfghjklmnpqrstvxyz':
            qtd_consoantes = str.upper(frase[i])
        i = i + 1
        return qtd_consoantes