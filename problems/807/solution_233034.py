def conta_frases(x):
    frases=x
    if frases.count('...')>0:
        return frases.count('.')+frases.count('!')+frases.count('?')+frases.count('...')-3*frases.count('...')

    else:
        return frases.count('.')+frases.count('!')+frases.count('?')