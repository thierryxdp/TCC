def uppCons(frase):
    """retorna uma frase com todas as suas consoantes em
    maiusculo dado uma str frase
    str -> str"""
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    lista = []
    i = 0
    while i < len(frase):
        if consoantes in frase[i]:
            lista += [str.upper(frase[i])
        i += 1
    return str.join('', lista)