def conta_frases(frases):
    frase1=str.split(frases,'...')
    f1=''.join(frase1)
    interrogacao=str.split(f1,'?')
    exclamacao=str.split(f1,'!')
    ponto=str.split(f1,'.')
    return len(f1)