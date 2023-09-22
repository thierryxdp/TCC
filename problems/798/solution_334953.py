def freq_palavras(frases):
    counter_dict = {}
	for palavra in frases:
        if palavra not in counter_dict:
    		counter_dict[palavra] = frases.count(palavra)
    return counter_dict