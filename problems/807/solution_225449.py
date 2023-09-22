def conta_frases(frase):
    if '.'=='...':
        return str.count(frase,'...')+str.count(frase,'!')+str.count(frase,'?')