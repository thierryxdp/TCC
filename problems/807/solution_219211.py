def conta_frases(string):
    "Pega uma string e retorna quantidade de frases"
    frases = str.split(str.split(str.split(str.split(string, '!'), '?'), "..."), '.')
    return len(frases)