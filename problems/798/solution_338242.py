def freq_palavras(frases):
    dic={}
    tempdic={}
    
    palavra = frases.split(' ')
    for x in range(0,len(palavra)):
    	if palavra[x] in dic:
        	dic[palavra[x]]+=1
        	x=x+1
        else:
            tempdic = {palavra[x]:1}
            dic.update(tempdic)
            x=x+1
    return dic