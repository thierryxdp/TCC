def freq_palavras(frases):
    counter_dict = {}
	for palavra in frases.split():
        if palavra not in counter_dict:
    		counter_dict[palavra] = frases.split.count(palavra)
    return counter_dict