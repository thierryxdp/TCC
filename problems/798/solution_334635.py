def freq_palavras(frase):
    
    dicionario={}
    palavras= frase.split()
    
    for palavra in palavras:
        value= list.count(palavras,palavra)
        dicionario[palavra]=value
        
	return dicionario