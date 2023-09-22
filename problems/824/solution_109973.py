def uppCons(frase):
    '''.'''
    letras=(letra.upper() if letra in 'bcdfghjklmnpqrçstvwxz' else letra for letra in frase)
    return letras