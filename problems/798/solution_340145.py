def freq_palavras(frases):
    ls=str.split(frases)
    r={}
    for e in ls:
        r.append(e,list.count(ls,e))
    return r