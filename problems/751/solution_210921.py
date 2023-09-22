def conta_frases(frase):
    return str.count(frase,'!') + str.count(frase,'?') + str.count(frase,'...') + (str.count(frase,'.')-3*str.count(frase,'...'))
def quant_palavras(frase):
    return len(str.split(frase))