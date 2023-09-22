def freq_palavras(frase):
    '''str->dict'''
    dicionario={}
    for x in frase:
       	quantidade=frase.count(x)
    	dicionario[frase]=quantidade
    return dicionario