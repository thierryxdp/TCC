def freq_palavras(frases):
    
    palavras = frases.split()
    dicionario = {}
    
    for i in palavras:
        cont = palavras.count(i)
        dicionario.update({i:cont})
        return dicionario