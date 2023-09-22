def uppCons(frase):
    """Retorne a frase com todas as suas consoantes minúsculas"""
    i = 0
    qtd_consoantes = ''
    while frase:
        if frase[i] in 'BCDFGHJKLMNPQRSTVXYZbcdfghjklmnpqrstvxyz':
            nova_frase =str.upper(frase[i])
        i = i + 1
        return nova_frase