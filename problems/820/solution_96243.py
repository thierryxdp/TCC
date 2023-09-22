def posLetra(frase, letra, ocorrencia):
    i = 0
    posicao = [] 
    onde_esta = frase.index(letra)
    
    while i<len(frase): 
        if frase[i] is letra:
            posicao += ([onde_esta],)
        i += 1
        posicaodaletra = str.posicao[ocorrencia]
    return posicaodaletra