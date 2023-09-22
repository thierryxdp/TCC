def uppCons(frase):
    """recebe uma string e retorna a mesma string com todas as consoantes em maiusculo
    str -> str"""
    lista_frase = list(frase)
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    i = 0
    while i < len(frase):
        if frase[i] in consoantes:
            lista_frase[i] = lista_frase[i].upper()
        i += 1
    return ''.join(lista_frase)