def conta_frases(texto):
    quant= texto.count('...') 
    amor= texto.split('...')
    texto= ''.join(amor)
    quant2= texto.count('?')
    quant3= texto.count('.')
    quant4= texto.count('!')
    return quant+quant2+quant3+quant4