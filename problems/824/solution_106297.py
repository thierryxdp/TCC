def uppCons(frase):
    '''retorna a mesma frase porem com todas as consoantes em maiusculas
    str -> str'''
    i = 0
    while i < len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxz':
            frase = str.replace (frase,frase[i], str.upper(frase[i]))
        i = i + 1
    return frase