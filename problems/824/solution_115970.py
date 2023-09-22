def uppCons(frase):
    """retorna uma frase com todas as suas consoantes em
    maiusculo dado uma str frase
    str -> str"""
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    nova_str = ''
    i = 0
    while i < len(frase):
        if frase[i] in consoantes:
            nova_str += str.upper(frase[i])
        else:
            nova_str += frase[i]
        i += 1
    return nova_str