def uppCons(frase):
    '''Função que recebe uma frase e a retorna com todas as suas consoantes em maiúsculas;
    str -> str'''
    i = 0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase = str.replace(frase,frase[i],str.upper(frase[i]))
        i=i+1
    return frase