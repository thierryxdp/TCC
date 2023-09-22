def freq_palavras (lista):
   
    dic={}
    n=1
    lista=str.split(frases)
    for p in lista:
        if p in dic:
            dic[p]=dict.get(dic,p)+1
        else:
            dic[p]=1
    return dic