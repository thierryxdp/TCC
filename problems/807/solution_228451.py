def conta_frases(frase):
    str.replace(frase,'...','Kaisa')
    return str.count(frase,'.')+str.count(frase,'?')+str.count(frase,'!')+str.count(frase,'Kaisa')