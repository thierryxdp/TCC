'''Programa recebe uma frase, e a retorna com todas suas consoantes
maiúsculas.
str -> str'''
def uppCons(frase):
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvxzçBCDFGHJKLMNPQRSTVXZÇ':
            frase = str.replace(frase, frase[contador], frase[contador].upper())
        contador = contador + 1
    return frase