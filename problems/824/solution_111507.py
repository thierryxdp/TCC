def uppCons(frase:str) -> str:
    '''retorna a frase dada com todas suas consoantes em maiúscula'''
    i=0
    cons=list()
    while(i<len(frase)):
        if (str.lower(frase[i]) in 'bcdfghijklmnpqrstvwxyz'):
            list.append(cons, str.upper(frase[i]))
        i+=1
    return cons