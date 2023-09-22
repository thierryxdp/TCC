def quant_palavras(frase):
    letras=str.split(frase,' ')
    return len(letras)
def conta_frases(frases):
    ponto=str.count(frases,'.')
    exclamação=str.count(frases,'!')
    interrogação=str.count(frases,'?')
    reticências=str.count(frases,'...')-str.count(frases,'.')+1
    frases1=ponto+exclamação+interrogação+reticências
    return frases1