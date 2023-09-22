def conta_frases(frases):
    return frases.count('. ')+frases.count('?')+frases.count('!')+frases[-1:].count('.')