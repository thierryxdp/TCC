def uppCons(frase):
    ''' Funcao que recebe uma frase e retorna todas as consoantes maiusculas
str->str'''
    return ''.join(caractere.upper() if caractere in 'bcdfghjklmnpqrstvxwyzç' else caractere for caractere in frase)