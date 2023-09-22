def uppCons (frase):
    '''recebe uma frase e retorna a frase com suas consoantes em caixa-alta;
    str->str'''
    b=''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            b=b+str.upper(frase[i])
        else:
            b=b+frase[i]
        i=i+1
    return b