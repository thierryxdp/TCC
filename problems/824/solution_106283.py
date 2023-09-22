def uppCons(frase):
    '''funcao que recebe uma frase e retorna essa mesma frase com todas as suas consoantes em maiusculo
    str->str'''
    i = 0
    consoantes=' '
    while i<len(frase):
        if frase[i] in 'qrtpsdfghjklzxcvbnm':
        	consoantes = consoantes + str.upper(frase[i])
            i=i+1
    return consoantes