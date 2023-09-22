def freq_palavras(text):
    x=text.split(' ')
    i=0
    dic={}
    for i in range(len(x)):
        substring=tec[i]
        text.count(substring)
        dic[tec[i]]=text.count(substring)
    i=i+1
    return dic