def conta_frases(frases):
    x=frases.split('?') or frases.split('.') or frases.split(!) or frases.split('...')
    return len(x)