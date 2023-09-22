def freq_palavras(text):
    x=text.split()
    print(text)
    i=0
    dic={}
    for i in range(len(x)):
        print(i)
        tec=text.split()
        print(tec)
        substring=tec[i]
        print(substring)
        text.count(substring)
        dic[tec[i]]=text.count(substring)
        print (dic)
    i=i+1
    return dic