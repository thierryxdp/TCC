def uppCons(frase):
    """retorna a frase com suas consoantes em maiúscula"""
    """str -> str"""
    consoantes = ('bcdfghjklmnpqrstvwxyzç')
    i = 0
    nova_frase = ''
    while i < len(frase):
        if frase[i] in consoantes:
            nova_frase += str.upper(frase[i])
        else:
            nova_frase += frase[i]
        i += 1
    return nova_frase