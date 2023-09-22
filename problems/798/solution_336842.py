def freq_palavras(text):
    x=text.split(' ')
    dic={}
    for i in range(len(x)):
        substring=x[i]
        text.count(substring)
        dic[x[i]]=x.count(substring)
    return dic