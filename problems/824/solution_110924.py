def uppCons(frase):
    """Dado uma frase, transforma todas as consoantes em maiusculas. string>string"""
    i = 0
    frasef = ''
    while i<(len(frase)):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            frasef += str.upper(frase[i])
        else:
            frasef += frase[i]
        i += 1
    return frasef