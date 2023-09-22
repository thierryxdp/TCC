def uppCons(frase):
    '''Recebe uma frase e retorna a frase com todas as suas consoantes em maiúsculas.
    str-> str''' 
    i=0
    c= 'bcdfghjklmnpqrstvwxyz' 
    d= 'BCDFGHJKLMNPQRSTVWXYZ'
    while i<len(frase):
        if str.lower(frase[i]) in c:
            frase[i]= d[str.find(c,frase)]

        i+=1
    return frase