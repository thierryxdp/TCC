def uppcons(frase):
    '''Função que recebe um str(frase);
e retorna a str frase original com todas as consoantes em maiúsculo.
str-> str'''
    i = 0
    s = ' '
    frase.split( )
    while i < len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            s = s + str.upper(frase[i])
            i = i+1
        else:
            s = s + frase[i]
            i = i +1
    return s