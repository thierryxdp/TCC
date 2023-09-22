def uppCons(frase):
    """função que retorna a frase dada com todas as suas consoantes em maiúsculas
    str -> str"""
    indice = 0
    while indice < len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
           frase = str.replace(frase,frase[indice],str.upper(frase[indice]))
        indice += 1
    return frase