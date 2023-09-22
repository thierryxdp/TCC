def freq_palavras(frases):
    ''' docs
    str --> dict'''
    
    freq = dict()
    palavras = str.split(frases, ' ')
    
    for palavra in palavras:
        if palavra in freq:
			# se a palavra já existe, soma 1
            freq[palavra] += 1
        else:
            # se a palavra não existe, é a primeira, logo 1
            freq[palavra] = 1
    
    return freq