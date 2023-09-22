def conta_frases(frases):
    frase1=str.split(frases,'...')
    frase2=str.split(frases,'!')
    frase3=str.split(frases,'?')
    return len(frase1)-1+len(frase2)-1+len(frase3)-1