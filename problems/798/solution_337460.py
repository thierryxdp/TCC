def freq_palavras(frases):
    """
    string -> dicionario"""
    
    palavras = str.split(frases, " ")
    list.sort(palavras)
    dicionario=dict()
    ocorrencia = 0
    item = ""
    i = 0
    
    for i in palavras:
        
        item = palavras[i]
        ocorrencia = list.count(palavras, item)
    	
        
        dicionario= dicionario+{item:ocorrencia}
        
        i = i + ocorrencia -1
        
        
    
    return dicionario