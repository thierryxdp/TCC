def freq_palavras (frases):
    d=[]
    for p in str.split(frases):
    	d[p]= dict.get(d,p,o) +1
    return d