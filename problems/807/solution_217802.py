def conta_frases(string):
    frase=str.split(string,'...')
    f1=len(frase)
    frase2=str.split('frase','.')
    f2=len(frase2)
    frase3=str.split(string,'?')
    f3=len(frase3)
    return (f1-1)+(f2)+(f3-1)