def freq_palavras(frases): 
    palavras = frases.split() 
    freq = {}
    
    for palavra in palavras: 
        ocorrencia = palavras.count(palavra)
        freq[palavra] = ocorrencia
    
    return freq