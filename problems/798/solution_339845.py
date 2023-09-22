def freq_palavras(frases):
    
    palavras = frases.split()
    dicionario = {}
    i = 0
    for i in palavras:
        cont = palavras.count(i)
        dicionario.update({i:cont})
        return dicionario