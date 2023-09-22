def freq_palavras(frases):
    """
    string -> dicionario"""
    
    palavras = str.split(frases, " ")
    list.sort(palavras)
    dicionario=dict()
    
    for i in palavras:
        
        ocorrencia = list.count(palavras, palavras[1])
    	item = palavras[i]
        
        dicionario= dicionario+{item:ocorrencia}
        
        i = i + ocorrencia -1
        
        
    
    return dicionario