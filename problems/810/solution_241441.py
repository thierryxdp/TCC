def inverte (frase):
    frase=frase.replace('.',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('-',' ')
    frase=str.lower(frase)
    palavras=frase.split( )
    palavras.reverse( )
    return ' '.join(palavras)
'''funcao que inverte, remove pontuacoes e
letras maiusculas de uma frase
str->str'''