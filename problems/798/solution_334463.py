def freq_palavras(frase):
    '''str->dict'''
    dicionario={}
    for x in frase:
       	quantidade=frase.count(x)
    	dicionario=dicionario +x[quantidade]
    return dicionario