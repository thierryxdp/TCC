def uppCons(frase):
    '''Recebe uma frase e retorna a frase com todas as suas consoantes em maiúsculas.
    str-> str''' 
    i=0
    while i<len(frase):
        if str.lower(frase[i:i+1]) in 'bcdfghjklmnpqrstvwxyz': 
            frase[i:i+1] = str.upper(frase[i:i+1])
        i+=1
    return frase