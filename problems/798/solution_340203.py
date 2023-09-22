def freq_palavras(frases):
'''str --> dict
	'''
	frase = str.split(frases,'')
    freq = {}
    
    for p in frase:
        freq[p] = list.count(frase,p)
    return freq