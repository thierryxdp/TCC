def conta_frases(texto):

    substituidor1 = texto.replace('...', '/')
    substituidor2 = substituidor1.replace('?', '/')
    substituidor3 = substituidor2.replace('!', '/')
    substituidor4 = substituidor3.replace('.', '/')
    splitador = substituidor4.split('/')
    quant_frases = len(splitador) - 1
    
    return quant_frases