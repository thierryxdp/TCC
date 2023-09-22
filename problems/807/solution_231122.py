def quant_palavras(frase):
    letras=str.split(frase,' ')
    return len(letras)
def conta_frases(frases):
    ponto=str.count(frases,'.')
    exclamacao=str.count(frases,'!')
    interrogacao=str.count(frases,'?')
    reticencias=str.count(frases,'...')-str.count(frases,'.')+1
    frases1=ponto+exclamacao+interrogacao+reticencias
    return frases1