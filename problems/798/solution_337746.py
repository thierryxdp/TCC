def freq_palavras(frases):
    freq = {}
	frase_list = frases.split(' ')
    for i in range(len(frase_list)):
        freq = {frase_list[i]: frase_list.count(frases_list[i])}
    return freq