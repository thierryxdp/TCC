def conta_frases(frases):
    frase1=str.split(frases,'...')
    f1=''.join(frase1)
    frase2=str.split(f1,'?')
    return len(frase2)