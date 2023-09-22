def freq_palavras(text):
    text.split()
    i=0
    dic={}
    for i in range(len(text)):
        tec=text.split()
        substring=tec[i]
        text.count(substring)
        dic[tec[i]]=text.count(substring)
	i+=1
    return dic