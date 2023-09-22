def conta_frases(string):
    frase=str.split(string,'...')
    f1=len(frase)
    frase2=str.split(string,'.')
    f2=len(frase2)
    frase3=str.split(string,'?')
    f3=len(frase3)
    frase4=str.split(string,'!')
    f4=len(frase4)
    return frase