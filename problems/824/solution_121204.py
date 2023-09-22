def uppCons(frase):
    '''Recebe uma frase e retorna a frase com todas as suas consoantes em maiúsculas.
    str-> str''' 
    i=0
    c= 'bcdfghjklmnpqrstvwxyz' 
    d= 'BCDFGHJKLMNPQRSTVWXYZ'
    while i<len(frase):
        if str.lower(frase[i]) in c:
            e=0
            while e<len(c):
                if str.lower(frase[i])==c[e]:
                    frase[i]=d[e]
            e+=1

        i+=1
    return frase