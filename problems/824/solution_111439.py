def uppCons(frase):
    '''Recebe uma frase e retorna com suas consoantes maiusculas.str->str'''
    l=''.join(l.upper() if l in 'bcdfghjklmnpqrçstvwxz'else l for l in frase)
    return l