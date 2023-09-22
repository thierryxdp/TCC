def uppCons(frase):
    '''
    função que recebe uma frase e retorna todas as suas consoantes em maiúsculas;
    str -> str
    '''
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            str.replace(frase,frase[i],str.upper(frase[i]))
        i = i + 1
    return frase