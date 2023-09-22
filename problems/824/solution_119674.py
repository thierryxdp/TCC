def uppCons(frase):
    ''' Retona a frase com todas as suas consoantes em maiúsculas '''
    s=''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            f= frase[i].upper()
            s= s + f
        else:
            s=s+frase[i]
        i=i+1
    return s