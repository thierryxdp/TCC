def conta_frases(frases):
    frase1=str.strip(frases,'...')
    f=str.split(frase1,'?')
    f1=str.split(frase1,'!')
    f2=str.split(frase1,'.')
    
    frase=str.split(frases,'...')
    ff=len(frase)-1
    return ff+(len(f)-1)