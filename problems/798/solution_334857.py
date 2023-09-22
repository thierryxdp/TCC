def freq_palavras(frases):
    dic={}
    nfrases= str.find(frases[0:-1])
    for f in nfrases: 
        dic[f]=1 
    return dic