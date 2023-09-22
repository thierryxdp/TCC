def conta_frases(frase):
    if '.' in not frase:
        return str.count(frase,'!')+str.count(frase,'?')+str.count(frase,'...')