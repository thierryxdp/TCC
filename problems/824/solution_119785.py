def uppCons(frase):
    '''dada uma frase retorna a frase com todas as suas consoantes em maiúsculas
    string->string'''
    i=0
    FRASE=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            FRASE = FRASE + str.upper(frase[i])
        else:
            FRASE = frase[i]
        i = i+1
    return FRASE