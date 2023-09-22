def posLetra(string,letra,n):
	i=0
	ocorr=[]
	if str.count(string,letra)<n:
		return -1
	while len(ocorr)<n:
		if string[i]==letra:
			ocorr.append(string[i])
		i+=1
	return i-1