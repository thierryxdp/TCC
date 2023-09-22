def uppCons(frase):
    '''funcao que recebe uma frase e retorna essa mesma frase com todas as suas consoantes em maiuscula
    str->str'''
    consoantes=[]
    i = 0
    consoantes=' '
    while i<len(frase):
        if frase[i] in 'qrtpsdfghjklzxcvbnm':
            str.upper(frase[i])
            consoantes= consoantes + [frase[i]]
        i=i+1
    return consoantes