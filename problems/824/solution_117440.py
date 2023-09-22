def uppCons(frase):
    '''funcao que recebe uma frase e retorna a frase com suas consoantes em maiusculas e o resto sem alteracao
    str->str'''
    i=0
    consoantes=''
    while i<len(frase):
        if 'BCDFGHJKLNMPQRSTVWXYZbcdfghjklnmpqrstvwxyz' in frase[i]:
            consoantes=str.upper(consoantes)+ str.lower(frase[i])
        i=i+1
        if 'AEIOUaeiou' in frase[i]:
            consoantes=str.lower(frase[i])
        i=i+1
    return consoantes