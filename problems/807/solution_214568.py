def conta_frases(frases):
    interrogaçao = str.count(frases, '?')
    exclamaçao = str.count(frases, '!')
    ponto = str.count(frases, '.')
    #... = str.find(frases, '...')
    return interrogaçao + exclamaçao + ponto