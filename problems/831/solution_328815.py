def consoante(letra):
    if letra.lower() in 'bcdfghjklmnpqrstvwxyzç':
        return True
    return False

def lingua_p(palavra):
    '''comentario padra
    e1, e2 -> s'''
    palavra_p = ''
    for letra in palavra:
        letra_m = letra.lower()
        palavra_p += letra_m
        if not consoante(letra_m):
            palavra_p += 'p' + letra_m
    return palavra_p