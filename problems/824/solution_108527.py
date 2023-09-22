def uppCons(frase):
    """ funcao que recebe uma frase e retorna a frase com todas as consoantes em maiusculas
    str->str"""
nova_frase=' '
indice=0
while indice<len(frase):
    letra= frase[indice]
    if letra in 'bcdfghjklmnpqrstvxwyz':
        letra= str.upper(letra)
    nova_frase= nova_frase + letra
    indice= indice+1
return nova_frase