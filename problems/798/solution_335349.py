def freq_palavras(frases):
    a = str.split(freq_palavras)
    n = len (a)
    b = 0
    resp = {}
    for palavra in range (n):
        palavra = a[b] 
        b += 1
		resp += {palavra:str.count(frases,b),}
	return resp