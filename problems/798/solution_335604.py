def freq_palavras(palavra): 
    dic={}
    lista=str.split(palavra) 
    for p in lista: 
        dic[p]=1 
    return dic