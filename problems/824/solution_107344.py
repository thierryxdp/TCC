def uppCons (frase):
    '''Funçao que retorna a frase com todas as suas consoantes em maiuscula.
    str -> str'''

    frase = list(frase)
    indice = 0
    f = ()
    while indice< len(frase):
        if 'aeiouAEIOU' not in frase[indice]:
            frase1 = frase[indice]
            frase1 = str(frase1)
        indice += 1
    f = str(f)
    return f