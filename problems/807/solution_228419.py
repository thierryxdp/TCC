def conta_frases(frase):
    if '...' in frase:
        return str.count(frase,'.',0,30)+str.count(frase,'?')+str.count(frase,'!')+str.count(frase,'...')