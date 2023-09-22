def freq_palavras(frases):
    fraseLista=frases.split(' ')
    dic={}
    i=0
    while i<len(fraseLista):
        n=fraseLista.count(fraseLista[i])
        dic={fraseLista[i]:n}
        i=i+1
    return dic