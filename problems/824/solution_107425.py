def uppCons (frase):
    '''Funçao que retorna a frase com todas as suas consoantes em maiuscula.
    str -> str'''
    
    i = 0
    while i <= len(frase):
        if 'aeiouAEIOU' not in frase [i]:
            frase1 = frase[i]
            str.upper(frase1)
        i += 1
    return frase1