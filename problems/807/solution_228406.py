def conta_frases(frase):
    return str.find(frase,'.')+ str.count(frase,'?')+ str.count(frase,'!')+str.count(frase,'...')