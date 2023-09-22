def conta_frases(frase):
    return str.replace(frase,'.','...')(str.count(frase,'.')+str.count(frase,'!')+str.count(frase,'?'))