def uppCons(frase):
    """Dada uma frase, retorna a frase com as consoantes em maiúsculo, e os outros caracteres exatamente como estavam"""
    x = 0
    y = ''
    while x < len(frase):
        if frase[x] in 'bcçdfghjklmnpqrstvwxyz':            
            y = y + str.upper(frase[x])
        else:
            y = y + frase[x]
        x = x + 1
    return y