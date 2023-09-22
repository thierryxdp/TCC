def uppCons(frase):
    '''funcao que recebe uma frase e retorna a frase com suas consoantes em maiusculas e o resto sem alteracao
    str->str'''
    i=0
    consoantes=''
    vogais=''
    while i<len(frase):
        if frase[i] in'AEIOUaeiou'and 'BCDFGHJKLNMPQRSTVWXYZbcdfghjklnmpqrstvwxyz':
            consoantes=str.upper(consoantes)+vogais+frase[i]
        i=i+1
    return consoantes+vogais
    while i<len(frase): 
        if frase[i] in 'AEIOUaeiou':
            vogais=vogais+frase[i]
        i=i+1
    return vogais