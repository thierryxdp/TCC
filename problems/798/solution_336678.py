def freq_palavras(frase):
    i=0
    dic={}
    for i in len(frase):
        tec=text.split()
        substring=tec[i]
        text.count(substring)
        dic[tec[i]]=text.count(substring)
	i+=1
    return dic