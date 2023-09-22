def uppCons(frase):
    '''
       Dada uma frase a função retorna a frase com as 
       consoantes em maiísculas 
       str -> str
    '''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            str.upper(frase[i])
        i = i + 1
    return frase[i]