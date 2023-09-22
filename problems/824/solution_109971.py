def uppCons(frase):
    '''.'''
    letras=''.join(letra.upper() if letra in 'bcdfghjklmnpqrçstvwxz',else letra for letra in frase)