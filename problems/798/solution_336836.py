def freq_palavras(text):
    x=text.split(' ')
    i=0
    dic={}
    for i in range(len(x)):
        tec=text.split(' ')
        print(tec)
        substring=tec[i]
        text.count(substring)
        dic[tec[i]]=text.count(substring)
        print(dic)
    i=i+1
    return dic