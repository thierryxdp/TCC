def conta_frases(frases):
    ''' função que conta o numero de frases de um texto determinados pelas caracteres especiais ('...', '!', '?', '.' - sem repetições das mesmas)
str -> int'''
    return frases.count("!") + frases.count("?") + frases.count(".[1]") + frases.count("...")