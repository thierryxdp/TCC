def uppCons (frase):
    '''Funçao que retorna a frase com todas as suas consoantes em maiuscula.
    str -> str'''

    frase = list(frase)
    indice = 0
    
    while indice < len(frase):
        if 'bcdfghjklmnpqrstvxwyz' in frase[indice]:
            frase1 = frase[indice]
            frase1 = str.upper(frase)
            frese1 = str.join (frase)
            f = f+frase1
        indice += 1
   
    return frase1