def uppCons(frase):
    """ Recebe uma frase de entrada e retorna a frase com todas as consoantes em maiúsculas;
    string->string """
    i=0
    frase2=''
    while i<len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            frase2 += frase[i].upper()
        else:
            frase2+=frase[i]
        i=i+1
    return frase2