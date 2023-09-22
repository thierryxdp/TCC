def freq_palavras(frase):
    dic={}
    lista=str.split(frase,' ')
    for chave in lista:
        if chave in list(dict.keys(dic)):
            dic[chave]=dic[chave]+1
            
        else:
            dic[chave]=1
            
    return dic