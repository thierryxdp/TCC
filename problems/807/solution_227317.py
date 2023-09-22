def conta_frases(frase):
    f1=len(frase.split('...',))
    f2=len(frase.split('?'))
    f3=len(frase.split('!'))
    return len(f1+f2+f3)