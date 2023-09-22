def conta_frases(frase):
    if str.find(frase,'...','.'):
    return str.count(frase,'.')+str.count(frase,'!')+str.count(frase,'?')+str.count(frase,"...")