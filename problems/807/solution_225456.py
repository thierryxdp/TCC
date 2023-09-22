def conta_frases(frase):
    if frase in not '...':
        return str.count(frase,'.')+str.count(frase,'!')+str.count(frase,'?')
    else:
        return return str.count(frase,'.')+str.count(frase,'...')+str.count(frase,'!')+str.count(frase,'?')-2