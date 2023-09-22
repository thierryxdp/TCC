def uppCons(frase):
    '''
    funcao que recebe uma frase de entrada e retorna
    essa mesma frase mas com todas suas consoantes em
    letras maiusculas e as outras letras continuam do
    mesmo jeito
    str->str
    '''
    x=1
    string=''
    while x<len(frase):
        if frase[x] in 'bcdfghjklmnpqrstvwxyz':
            string=string+frase[x].upper()
        else:
            string=string+frase[x].lower()
        x=x+1

    return frase[0]+string