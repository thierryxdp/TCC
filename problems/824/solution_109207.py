def uppCons(frase):
    '''Funco que recebe uma frase e retorn mesma com todas as suas
    consoantes em maiusculas e os demais caracteres exatamente como estavam.'''
    i = 0

    while i < len(frase):
        if frase[i] not in 'aeiouAEIOUÃ£Ã¡Ã Ã©Ã¨Ã­Ã³Ã´Ãº':
            frase = frase.replace(frase[i],frase[i].upper())
        i = i+ 1
    return frase