def uppCons(frase):
    '''Recebe uma frase e retorna a frase com todas as suas consoantes em maiúsculas.
    str-> str''' 
    i=0
    c= 'bcdfghjklmnpqrstvwxyz' 
    d= 'BCDFGHJKLMNPQRSTVWXYZ'
    while i<len(frase):
        e=0
        while e<len(c):
            if frase[i]==c[e]:
                frase[i:i+1]= d[e]
            e=e+1


        i+=1
    return frase