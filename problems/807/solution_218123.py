def conta_frases(frases):
    frase1=str.strip(frases,'...')
    qtretic=str.split(frases,'...')
    return len(qtretic)-1