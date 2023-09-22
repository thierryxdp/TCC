def freq_palavras(frase):
    
    dicionario={}
    palavras= frase.split()
    
    for palavra in 'frase':
        key= palavra
        value= frase.count(palavra)
        dicionario[key]=value
        
	return dicionario