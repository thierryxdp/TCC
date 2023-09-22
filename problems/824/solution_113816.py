def uppCons(frase):
    """ Recebe como entrada uma frase e retorna a frase com todas as suas consoantes em maiúsculas 
    str -> str """
    consoantes = 'bcçdfghjklmnpqrstvwxyz'
    i=0
    while i<len(frase):
        if(frase[i] in consoantes):
            frase=frase[:i]+frase[i].upper()+frase[i+1:]
        i+=1
    return frase