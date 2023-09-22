def freq_palavras(frases):
    plvs=frases.split()
    ind=1
    dic={}
    while ind<=len(frases):
        if plvs[ind] in dic:
            dic[plvs[ind]]+=1
        else:
            dic[plvs[ind]]=1
        ind+=1
    return dic