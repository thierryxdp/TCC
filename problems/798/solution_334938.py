def freq_palavras(frases):
    counter_dict = {}
	for palavra in frases.split():
        if not palavra in counter_dict:
    		counter_dict[palavra] = frases.count(palavra)
    return counter_dict