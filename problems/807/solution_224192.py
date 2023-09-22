def conta_frases(frase):
    a = frase.count ('.')
    b = frase.count ('!')
    c = frase.count ('?')
    d = frase.count (a*3)
    return a + b + c + d