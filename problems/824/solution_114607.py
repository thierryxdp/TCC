def uppCons(frase):
    '''
        Dada uma string retorna a string com todas as consoantes em maiúsculo.
        str -> str
    '''
    i=0
    letra=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            frase= str.replace(frase,frase[i],str.upper(frase[i]))
        i=i+1
    return frase