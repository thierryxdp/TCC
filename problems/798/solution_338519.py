def freq_frases(x):
    l=str.split(x)
    dic={}
    for i in l:
        dic.update({i:list.count(i)})
    return dic