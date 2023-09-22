def freq_palavras(frases):
    plvs=frases.split()
    ind=0
    dic={}
    while ind<len(plvs):
        if plvs[ind] in dic:
            dic[plvs[ind]]+=1
        else:
            dic[plvs[ind]]=1
        ind+=1
    return dic