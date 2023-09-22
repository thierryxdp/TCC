def freq_palavras(frases):
    i =0
    k=0
    j=0
    dic={}
    for chave in frases:
        if str.count(frases,frases[j],0) ==i:
            dic[frases[j]]=i
            k=k+1
    return dic