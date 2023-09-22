def freq_palavra(frase):
    
    dicionario={}
    
    for palavra in frase:
        key= palavra
        value= frase.count(palavra)
        dicionario[key]=value
        
   	return dicionario