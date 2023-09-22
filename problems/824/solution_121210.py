def uppCons(frase):
    '''Recebe uma frase e retorna a frase com todas as suas consoantes em maiúsculas.
    str-> str''' 
    i=0
    c= 'bcdfghjklmnpqrstvwxyz' 
    nova=' '

    while i<len(frase):
        if str.lower(frase[i]) in c:
            nova+=str.upper(frase[i])
        else:
            nova+= frase[i]
            

    return nova