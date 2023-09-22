def conta_frases (frases):
    '''função que dada um texto, retorna a quantidade de palavras nela'''
    '''str -> int'''
    frases = frases.replace("!",".")
    frases = frases.replace("...",".")
    frases = frases.replace("?",".")
    frases = frases.split(".")
    return len(frases)-1