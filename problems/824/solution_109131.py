def uppCons(frase):
    '''Funcao que recebe como entrada uma frase e retorna a mesma com todas as suas consoantes em maiusculas.
    str -> str'''
    
    i = 0
    frase = list(frase)
    
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxyzwç':
            frase[i] = str.upper(frase[i])
        i += 1
    
    frase = str.join('', frase)
    
    return frase