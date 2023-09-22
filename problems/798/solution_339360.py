def freq_palavras(frase):
    '''retorna a frequencia das palavras em uma string
    str-> dict'''
    
    dicionario={}
    palavras= frase.split()
    
    for palavra in palavras:
        value= list.count(palavras,palavra)
        dicionario[palavra]=value
        
	return dicionario