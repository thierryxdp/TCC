def conta_frases (frase):
    teste = frase.remove("...")
    a = teste.count ('.')
    b = frase.count ('!')
    c = frase.count ('?')
    d = frase.count ('...')
    return a + b + c + d