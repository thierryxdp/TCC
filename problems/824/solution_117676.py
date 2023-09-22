def uppCons(frase):
    '''funcao que recebe uma frase e retorna a frase com suas consoantes em maiusculas e o resto sem alteracao
    str->str'''
    i=0
    consoantes=''
    while i<(len(frase)):
        if frase[i] in 'bcçdfghjklnmpqrstvwxyz':
            consoantes =(str.upper(frase[i]))
        if frase[i] in'AEIOUaeiou':
            consoantes =(frase[i]+consoantes)
        i=i+1
    return consoantes