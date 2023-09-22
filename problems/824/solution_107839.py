def uppCons(frase):
    '''Calcula e retorna uma frase nova, a partir de uma original, onde as consoantes estao maiusculas
       parameters:
       frase:frase original
    str->str'''
    maiuscula=''
    posicao=0
    while posicao<len(frase):
        letra=frase[posicao]
        if letra in 'bcdfghjklmnpqrstvwxyzç':
            letra=letra.upper()
        posicao=posicao+1
        maiuscula=maiuscula + letra
    return maiuscula