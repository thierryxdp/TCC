def freq_palavras(frase):
    
    dicionario={}
    palavras= str.maxsplit(frase)
    
    for palavra in palavras:
        key= palavra
        value= frase.count(palavra)
        dicionario[key]=value
        
	return dicionario