def freq_palavras(frases):
    dic={}
    nfrases= str.split(frases)
    i=0 
    while i < len(nfrases):
        palavra=nfrases[i] 
        dic[palavra]=1
    return dic