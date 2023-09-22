def freq_palavras(frase):
    '''str->dict'''
    dicionario={ }
    for key in frase:
       	value=frase.count(key)
       	dicionario.insert(key, value)
    	
    return dicionario