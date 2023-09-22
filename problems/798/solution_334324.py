def freq_palavras(frases):
    d={}
    l=frases.split()
    for x in l:
        if x not in d:
            d[x]=1
		else:
            d[x]+=1
	return d