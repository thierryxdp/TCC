def conta_frases(frases):
    frase1 = str.replace(frases, ('?','...','.','!'),'.')
    frase2 = str.split(frases1,'.')
    return len(frase2)