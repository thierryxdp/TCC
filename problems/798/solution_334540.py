def freq_palavras(frase):
    dic={}
    for chave in frase:
        if chave in list(dict.keys(dic)):
            dic[chave]=dic[chave]+1
            
        else:
            dict.get(dic,chave,1)
            
    return dic