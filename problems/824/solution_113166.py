def uppCons(frase):
    ''' Fazer uma funcao que receba uma frase e retorne ela com consoantes em letra minusculas;
    list -> list'''
    
    i = 0
    
    while i < len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvxwyz':
            a = str.upper(frase[i])
            rep = str.replace(frase, frase[i],a)
            frase = rep
        i = i + 1
        
    return frase