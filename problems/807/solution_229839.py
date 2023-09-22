def conta_frases(texto):
    '''função que conta o numero de frases que aparecem em um  texto;
    str -> int'''
    frase1 = str.replace(texto,'.','')
    frase2 = str.replace(frase1,'!','')
    frase3 = str.replace(frase2,'?','')
    frase4 = str.replace(frase3,'...','')
    return frase4