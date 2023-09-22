def pontuacao():
    return '.?!...'

def conta_frases(frases):
    if str.count(frases, '.')>0:
        return str.count(frases, pontuacao[0])