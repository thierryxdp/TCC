def conta_frases(frases):
    interrogacao = str.count(frases, '?')
    exclamacao = str.count(frases, '!')
    ponto = str.count(frases, '. ')
    pontopontoponto = str.find(frases, '...')
    return interrogacao + exclamacao + pontopontoponto