def conta_frases(frase):
    b=str.replace(frase,'...','.')
    b+str.count(frase,'!')+str.count(frase,'?')