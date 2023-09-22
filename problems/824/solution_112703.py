def uppCons(frase):
    '''retorna a frase dada com todas as suas consoantes maiusculas'''
    '''str --> str'''
    
    f=''
    i=0
    while i < len(frase):
        if frase[i]  in 'bcdfghjklmnpqrstvwxyz':
            f = str.upper(frase[i])
        i = i + 1
    return f