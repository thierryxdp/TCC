def freq_palavras(frases):
    x=frases.split(' ')
    dc={}
    for i in range(len(x)):
        substring=x[i]
        frases.count(substring)
        dc[x[i]]=x.count(substring)
    return dc