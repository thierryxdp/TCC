def conta_frases(frase):
    f1=str.split(frase,'.')
    f2=str.split(frase,'!')
    f3=str.split(frase,'?')
    f4=str.split(frase,'...')
    t=([f1]+[f2]+[f3]+[f4])
    return t