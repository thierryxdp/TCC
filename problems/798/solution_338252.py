def freq_palavras(frases):
    dic={}
    tempdic={}
    
    palavra = frases.split(' ')
    for i in range(0,len(palavra)):
        if palavra[i] in dic:
            dic[palavra[i]]+=1
            i=i+1
    	else:
        tempdic = {palavra[i]:1}
        dic.update(tempdic)
        i=i+1
        return dic