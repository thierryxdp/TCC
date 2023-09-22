def freq_palavras(frases):
    counter_dict = {}
	for palavra in frases.split():
        if palavra not in counter_dict:
    		counter_dict[palavra] = frases.count(palavra)
        if palavra in counter_dict:
            counter_dict[palavra] =0
    return counter_dict