def uppCons(frase):
    """ Recebe uma frase e retorna a frase com todas as consoantes em maiúsculo;
    string->string """
    frase2=''
    for x in frase:
        if x in 'bcçdfghjklmnpqrstvwxyz':
            frase2+=x.upper()
        else:
            frase2+=x
    return frase2