def conta_frases(frases):
    frase1=str.strip(frases,'...')
    f=str.split(frase1,'?')
    f1=str.split(frase1,'!')
    f2=str.split(frase1,'.')
    return len(f)+len(f1)+len(f2)-3