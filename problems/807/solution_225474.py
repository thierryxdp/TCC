def conta_frases(frase):
    if str.replace(frase,'...','.'):
    return str.count(frase,'.')+str.count(frase,'!')+str.count(frase,'?')