def uppCons(frase):
    '''Recebe uma frase e retorna a mesma com suas consoantes maiusculas.str->str'''
    letras=''.join(letra.upper() if letra in 'bcdfghjklmnpqrçstvwxz' else letra for letra in frase)
    return letras