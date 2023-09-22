def uppCons(frase):
    
    ''' Função que, dada uma frase, retorna
        esta com todas as suas consoantes em
        maiúsculas.
        str -> str '''
    
    i = 0
    
    while i < len(frase):
        
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZ':
            frase = frase.replace(frase[i], frase[i].upper())
        
        i = i + 1
        
        return frase