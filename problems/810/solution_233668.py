def inverte (frase):
    '''funcao que inverte a frase dada e retorna outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiusculas e sem pontuacao
    str->str'''
    frase = str.lower(frase)
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    lista1 = str.split(frase, ' ')
    list.reverse()