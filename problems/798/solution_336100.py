def freq_palavras(frases):
    palavras = frases.split()
    i = 0
    for elem in palavras:
        n = list.count(palavras,elem)
		d1[i]={elem:n}
        i +=1
	return d1