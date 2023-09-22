def conta_frases (frase):
    teste = str.replace(frase,"...", 'briga')
    a = teste.count ('.')
    b = frase.count ('!')
    c = frase.count ('?')
    d = frase.count ('...')
    return a + b + c + d