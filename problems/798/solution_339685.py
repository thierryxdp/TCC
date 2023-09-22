def freq_palavras(frases):
    palavras = frases.split()
    dicionario = {}
    n = len(palavras)
    i = 1
    while i < n+1:
        contador = palavras.count(i)
        dicionario.update({i:contador})
        i += 1
    return dicionario