def freq_palavras(palavra): 
    dic={}
    lista=str.split(palavra) 
    for p in lista: 
        if p not in dic: 
            dic[p]=1 
        else p in dic: 
            dic[p]=+1
        
    return dic