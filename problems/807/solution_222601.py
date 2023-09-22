def conta_frases(frase):
    b=str.replace(frase,'...','.')
    str.count(b,'.')+str.count(frase,'!')+str.count(frase,'?')