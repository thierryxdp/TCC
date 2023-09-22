def uppCons(frase):
    '''Funcao que recebe uma frase, e retorna a mesma, porem com suas consoantes em maiusculas.
    Str -> Str'''
    
    tam = len(frase)
    frase2 = ''
    cont = 0
    
    while cont > 0:
        if frase[cont] in 'bcdfghjklmnpqrstvwxyzç':
            frase2 = frase2 + str.upper(frase[cont])
        else:
            frase2 = frase2 + frase[cont]
        cont = cont + 1
        
    return frase2