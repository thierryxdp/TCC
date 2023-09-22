def conta_frases(frases):
    if frases.count('...')>0:
        return frases.count('.')+frases.count('!')+frases.count('?')+frases.count('...')-3*frases.count('...')

    else:
        return frases.count('.')+frases.count('!')+frases.count('?')