def uppCons(frase):
    '''funcao que recebe uma frase e a transforma com todos os seus caracteres consoantes em maiuscula
    str->str'''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase=''
            frase=frase+str.upper[i]
        i=i+1
    return frase