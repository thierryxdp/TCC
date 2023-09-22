def conta_frases(frases):
    pontos = ('?','...','.','!')
    separador1 = str.split(frases,pontos)
    return len(separador1)