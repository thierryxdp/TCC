def uppCons(frase):
    ''' Funcao que recebe uma frase e retorna todas as consoantes maiusculas
str->str'''
    lowercase = 'bcçdfghjklmnpqrstvwxyz'
    uppercase = 'BCÇDFGHJKLMNPQRSTVWXYZ'
    tabela = str.maketrans(lowercase, uppercase)
    return frase.translate(tabela)