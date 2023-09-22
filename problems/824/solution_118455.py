def uppCons(frase):
    '''Função que retorna a frase de entrada com
    todas as consoantes em letras maiúsculas (as
    vogais se mantém da forma que foram inseridas)
    str -> str'''
    p = ''
    for consoante in frase:
        if consoante in 'bcçdfghjklmnpqrstvwxz':
            p += consoante.upper()
        else:
            p += consoante
    return p