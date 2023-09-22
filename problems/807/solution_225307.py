def conta_frases (frase):
    teste = str.replace(frase,"...", 'teste')
    x = teste.count ('.')
    y = frase.count ('!')
    w = frase.count ('?')
    z = frase.count ('...')
    return x + y + w + z