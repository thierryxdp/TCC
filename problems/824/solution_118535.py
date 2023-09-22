def uppCons(frase):
    '''
       Dada uma frase a função retorna a frase com as 
       consoantes em maiísculas 
       str -> str
    '''
    i=0
    consoante = ''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            consoante += str.upper(frase[i]) + frase
        i = i + 1
    return consoante