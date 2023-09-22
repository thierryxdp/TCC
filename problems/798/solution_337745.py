def freq_palavras(frases):
    freq = {}
	frase_list = frases.split(' ')
    for i in range(len(frases)):
        freq = {frase_list[i]: frase_list.count(frases_list[i])}
    return freq