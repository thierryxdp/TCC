def conta_frases(frase):
    str.replace(frase,'...','Kaisaaa')
    return str.count(frase,'.')+str.count(frase,'?')+str.count(frase,'!')+str.count(frase,'Kaisaaa')