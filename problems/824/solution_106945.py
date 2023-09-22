def uppCons(frase):
    '''retorna a mesma frase com todas as consoantes em maisculas
    str -> str'''
    r=''
    letra=''
    c=0
    consoantes='bcdfghjklmnpqrstvwxz'
    while c<len(frase):
        if frase[c] in consoantes:
            letra=str.upper(frase[c])
            r+=letra
        else:
            r+=frase[c]
        c+=1
        return r