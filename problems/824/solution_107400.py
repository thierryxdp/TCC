def uppCons (frase):
    '''Funçao que retorna a frase com todas as suas consoantes em maiuscula.
    str -> str'''

    frase = list(frase)
    indice = 0
    f = ()
    while indice < len(frase):
        if 'aeiouAEIOU' in frase[indice]:
            frase1 = frase[indice]
            frase1 = str.upper(frase1)
            f = f+frase1
        indice += 1
    f = str(f)
    return f