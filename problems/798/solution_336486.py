def freq_palavras(frases):
  	palavralist = frases.split()

  	palavras_freq = []
  	for w in palavralist:
    	palavras_freq.append(palavralist.count(w))

  	return ((dict(zip(palavralist, palavras_freq))))