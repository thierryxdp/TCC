def uppCons(frase): 
    '''Dado uma frase retorna a frase com todas as suas consoantes em maiúsculas. 
    str->str''' 
    i= 0
    nova=''
    while i < len(frase) :
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            nova+=str.upper(frase[i])
        else:
            nova+=frase[i]
        i+=1
    return nova