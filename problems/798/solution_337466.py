def freq_palavras(frases):
    """
    string -> dicionario"""
    
    palavras = str.split(frases, " ")
    list.sort(palavras)
    dicionario=dict()
    ocorrencia = 0
    item = ""
    
    
    for i in range(len(palavras)):
        
        item = palavras[i]
        ocorrencia = list.count(palavras, item)
    	
        dicionario[item] = ocorrencia
                    
    return dicionario