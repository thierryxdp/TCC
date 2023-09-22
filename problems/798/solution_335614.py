def freq_palavras(palavra): 
    dic={}
    n=2
    lista=str.split(palavra) 
    for p in lista: 
        if p not in dic: 
            dic[p]=1 
        else: 
            if p in dic: 
                dic[p]=n
                n+=1
    return dic