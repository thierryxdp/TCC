def uppCons(frase):
    '''Dada uma frase, retorna a mesma com somente as consoantes em maiusculo.
    str -> str'''
    i = 0
    consMaiusculas = ''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            consMaiusculas += frase[i].upper()
        else:
            consMaiusculas += frase[i]
        i += 1
    return consMaiusculas