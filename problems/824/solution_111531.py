def uppCons(frase:str) -> str:
    '''retorna a frase dada com todas suas consoantes em maiúscula'''
    i=0
    tudo = list()
    while(i<len(frase)):
        if frase[i]in 'bcdfghijklmnpqrstvwxyz':
            str.upper(frase[i])            
        i+=1
    return frase