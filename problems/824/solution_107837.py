def uppCons(frase):
    '''str->str'''
    maiuscula=''
    posicao=0
    while posicao<len(frase):
        letra=frase[posicao]
        if letra in 'bcdfghjklmnpqrstvwxyz':
            letra=letra.upper()
        posicao=posicao+1
        maiuscula=maiuscula + letra
    return maiuscula