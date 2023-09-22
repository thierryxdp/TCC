def conta_frase(frases):
    frases = frases.replace('!', '.')
    frases = frases.replace('?', '.')
    frases =  frases.replace('...', '.')
    return frases.count('.')