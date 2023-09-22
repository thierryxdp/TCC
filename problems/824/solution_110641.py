def uppCons(frase):
    '''Funcao que recebe uma frase e a retorna com todas as suas 
    consoantes em maiusculas e os demais caracteres exatamente como 
    estavam na frase original
    str -> str'''
    consoantes = ''
    i = 0
    Cminusculas = 'bcçdfghjklmnpqrstvwxyz'
    while i<len(frase):
        if frase[i] in Cminusculas:
            consoantes = consoantes + str.upper(frase[i])
        else:
            consoantes = consoantes + frase[i]
        i = i + 1
    return consoantes