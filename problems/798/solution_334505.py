def freq_palavras(frase):
    '''str->dict'''
    dicionario={ }
    for key in frase:
       	value=frase.count(key)
       	dict.apeend(dicionario,key, value)
    	
    return dicionario