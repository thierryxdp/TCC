def uppCons (frase):
    '''retona a frase com todas as consoantes em letras maiúsculas'''
    '''str->str'''
    
    i = 0
    frase = ' '
    
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            consoante=frase[i]
            i=i+1
            str.upper(
            return str.upper