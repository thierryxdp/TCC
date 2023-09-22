def freq_palavras(frases):
    palavras = frases.split()
    i = 0
    d1 = {}
    for elem in palavras:
        n = list.count(palavras,elem)
		d1[i]={elem:n}
        i +=1
	return d1