def conta_frases(frase):
    f1=str.split(frase,'.')
    f2=str.split(frase,'!')
    f3=str.split(frase,'?')
    f4=str.split(frase,'...')
    t=len(f1)+len(f2)+len(f3)+len(f4)
    return t