def freq_palavras(frases):
    palavras = frases.split()
    dicionario = {}
    n = len(palavras)
    i = 1
    while i < n+1 and x in palavras:
        contador = palavras.count(x)
        dicionario.update({x:contador})
        i += 1
    return dicionario