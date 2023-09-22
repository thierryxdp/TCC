def uppCons (frase):
    '''Funçao que retorna a frase com todas as suas consoantes em maiuscula.
    str -> str'''
    
    i = 0
    frase1 = 0
    while i <= len(frase):
        if frase [i] not in 'aeiouAEIOU':
            frase1 = frase[i]
            str.upper(frase1)
        i += 1
    return frase1