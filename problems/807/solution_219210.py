def conta_frases(string):
    "Pega uma string e retorna quantidade de frases"
    frases = str.split(string, '!')
    frases = str.split(frases, '?')
    frases = str.split(frases, '...')
    frases = str.split(frases, '.')
    return frases