def freq_palavras(palavra): 
    dic={}
    n=1
    lista=str.split(palavra) 
    for p in lista: 
        if p in dic: 
            dic[p]=n 
            n=n+1 
        else:
            dic[p]=1
    return dic