def conta_frases(frase):
    a = frase.count ('.')
    b = frase.count ('!')
    c = frase.count ('?')
    d = a*3
    return a + b + c + d