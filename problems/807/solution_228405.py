def conta_frases(frase):
    return str.index(frase,'.')+ str.count(frase,'?')+ str.count(frase,'!')+str.count(frase,'...')