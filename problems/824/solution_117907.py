def uppCons(frase):
    """Retorne a frase de entrada com todas as consoantes em maiúsculo"""
    frase_entrada = ''
    n = 0
    while n<len(frase):
        consoante = frase[n]
        if consoante in 'bcdfghjklmnpqrstvwxyzç':
            consoante = str.upper(consoante)
        frase_entrada = frase_entrada + consoante
        n = n + 1
    return frase_entrada