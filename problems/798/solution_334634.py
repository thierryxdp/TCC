def freq_palavras(frase):
    
    dicionario={}
    palavras= frase.split()
    
    for palavra in palavras:
        key= palavra
        value= list.count(palavras,palavra)
        dicionario[key]=value
        
	return dicionario