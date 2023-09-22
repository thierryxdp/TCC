def conta_frases(frase):
    import string
    pontuacao = string.punctuation
    return str.count(frase,pontuacao)