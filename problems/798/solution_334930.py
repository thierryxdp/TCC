def freq_palavras(frases):
    counter_dict = {}
	for palavra in frases.split():
        if palavra not in counter_dict:
    		counter_dict[palavra] = 0
        counter_dict[palavra] =+1
    return counter_dict