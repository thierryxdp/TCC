freq_palavras(frase):
    """
    string -> dicionario"""
    
    palavras = str.split(frase, " ")
    list.sort(frase)
    dicionario=dict()
    
    for i in palavras:
        
        ocorrencia = list.count(palavras, palavras[1])
    	item = palavra[i]
        
        dicionario= dicionario+{item:ocorrencia}
        
        i = i + ocorrencia -1
        
        
    
    return dicionario