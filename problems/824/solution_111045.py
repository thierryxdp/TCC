def uppCons(frase):
    '''Função que receba como entrada uma frase e retorne 
    a frase com suas consoantes em maiúsculas.
    string --> string.'''
    new=''
    t=0
    while t<len(frase):
        cons=frase[t]
        if cons in 'bcdfghjklmnpqrstvwxyzç':
            cons=str.upper(cons)
        new+=cons
        t+=1
    return new