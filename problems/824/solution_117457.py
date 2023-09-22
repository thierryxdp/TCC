def uppCons(frase):
    '''funcao que recebe uma frase e retorna a frase com suas consoantes em maiusculas e o resto sem alteracao
    str->str'''
    i=0
    consoantes=''
    while i<len(frase):
        if 'BCDFGHJKLNMPQRSTVWXYZbcdfghjklnmpqrstvwxyz' in frase[i]:
            str.upper(frase[i])
        consoantes=str.upper(consoantes)+(frase[i])
        if 'aeiou' in frase[i]:
            consoantes=str.replace('a','a').replace('e','e').replace('i','i').replace('o','o').relace('u','u')
        i=i+1
    return consoantes