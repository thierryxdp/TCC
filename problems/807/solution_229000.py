def conta_frases(frase):
    '''str->int
    de entra uma string que é separada e contada em frases terminadas com ponto, exclamação, reticencias e interrogação'''
    #str.split(str.replace(str.replace(str.replace(str.replace(str.replace(frase, '.','9'),'?','9'),'!','9'),'...','9'),'999','9'),'9')
    return len(str.split(str.replace(str.replace(str.replace(str.replace(str.replace(frase, '.','9'),'?','9'),'!','9'),'...','9'),'999','9'),'9'))-1