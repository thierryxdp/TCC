def freq_palavras(frases):
    dic={}
    nfrases= str.partition(frases,' ',',')
    for f in nfrases: 
        dic[f]=1 
    return dic