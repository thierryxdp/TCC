def uppCons(frase):
    '''funcao que recebe uma frase e retorna a frase com suas consoantes em maiusculas e o resto sem alteracao
    str->str'''
    i=0
    consoantes=''
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLNMPQRSTVWXYZbcdfghjklnmpqrstvwxyz':
            str.upper(frase[i])
        consoantes=str.upper(consoantes)+(frase[i])
        if 'AEIOU' in frase[i]:
            consoantes=str.replace('A','a').replace('E','e').replace('I','i').replace('O','o').relace('U','u')
        i=i+1
    return consoantes