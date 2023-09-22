def posLetra(frase, letra, ocorrencia):
    i = 0
    posicao = [] 
    ocorrencianalista = ocorrencia - 1
    onde_esta = frase.index(letra)
    
    while i<len(frase): 
        if frase[i] is letra:
            posicao += ([onde_esta],)
        i += 1
        else:
            return -1
    return posicao[ocorrencianalista]