def uppCons(frase):
    
    ''' funcao que recebe uma frase e a retorna com suas consoantes em 
        maiusculo
        str->str
    '''
    i=0
    cons= ''

    while i<len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            cons= cons+frase[i].upper()

        else:
            cons= cons+frase[i]
        
        i=i+1

    return cons