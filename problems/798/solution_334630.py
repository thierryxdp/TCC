def freq_palavras(frase):
    
    dicionario={}
    palavras= frase.split(-1)
    
    for palavra in palavras:
        key= palavra
        value= frase.count(palavra)
        dicionario[key]=value
        
	return dicionario