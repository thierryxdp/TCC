def conta_frases(frases):
    x=frases.split('?'),frases.split('.'),frases.split('!'),frases.split('...'),
    return x.count(len(x))