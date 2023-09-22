def uppCons(frase):
    '''Função que recebe uma frase e retorna a frase com todas as suas consoantes em maiusculas.
    str-->str'''
    i = 1
    frase2 = frase[:]
    letra = ''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz' :
            frase[i] = str.upper(frase[i])
        i = i +1
    return letra