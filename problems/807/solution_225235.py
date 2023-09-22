def conta_frases(string):
    '''Dada um frase (string) como parametro de entrada, substitui todas as pontuações de exclamação, interrogação e reticencias por pontos)'''
    s=string 
    s=str.replace(s,'!','.')
    s=str.replace(s,'?','.')
    s=str.replace(s,'...','.')
    x= str.count(s,'.')
    return x