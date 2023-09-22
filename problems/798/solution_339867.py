def freq_palavras(frases):
    p=frases.split()
    dic={}
    i=0
    while i<len(p):
        c=p.count(p[i])
        dic[p[i]]=c
        i+=1
    return dic