def freq_palavras(frases):
    """
    string -> dicionario"""
    
    palavras = str.split(frases, " ")
    list.sort(palavras)
    dicionario=dict()
    ocorrencia = 0
    item = ""
    
    for i in palavras:
        
        ocorrencia = list.count(palavras, palavras[i])
    	item = palavras[i]
        
        dicionario= dicionario+{item:ocorrencia}
        
        i = i + ocorrencia -1
        
        
    
    return dicionario