def porLetra(frase, letra, ocorrencia):
    i = 0
    posicao = [] 
    
    while i<len(frase): 
        if frase[i] is letra:
            posicao += frase.index(letra)
        i += 1
    return posicao[ocorrencia]