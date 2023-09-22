def uppCons(frase):
    '''Essa função recebe uma frase e retorna a frase com todas suas consantes em maiúsculas;
    Recebe uma frase;
    Retorna a frase com todas as suas consoantes em maiúsculas.
    str->str'''
    i=0
    n=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            n += str.upper(frase[i])
        else:
            n += frase[i]
        i=i+1
        
    return n
#Essa função recebe uma frase e retorna a frase com todas suas consantes em maiúsculas