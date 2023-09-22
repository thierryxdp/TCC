def inverte(texto):
    '''função que recebe uma frase e retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação;
    str -> str'''
    frase1 = frase.replace('-',' ')
    frase2 = frase1.replace(',',' ')
    frase3 = frase2.replace(':',' ')
    frase4 = frase3.replace(';',' ')
    frase5 = frase4.replace('.',' ')
    frase6 = frase5.replace('?',' ')
    frase7 = frase6.replace('!',' ')
    frase8 = frase7.lower()
    indice = str.count(frase8, '')
    frase9 = frase8[-1:indice]