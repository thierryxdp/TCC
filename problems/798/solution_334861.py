def freq_palavras(frases):
    dic={}
    nfrases= str.split(frases)
    i=0 
    while i < len(nfrases):
        dic[nfrases[i]]=+1 
    return dic