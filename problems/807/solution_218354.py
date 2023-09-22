def conta_frases(frases):
    frase= str.split(frases,'...')
    n1=len(frase)
    frasek=str.join('',frase)
    frase2=str.split(frasek,'.')
    n2=len(frase2)
    frase3=str.split(frases,'?')
    n3=len(frase3)
    frase4=str.split(frases,'!')
    n4=len(frase4)
    nT=(n1-1)+(n2-1)+(n3-1)+(n4-1)
    return nT