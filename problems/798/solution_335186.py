def freq_palavras(frases):
    '''...'''
    
    lista=str.split(frases)
    dic=''
    chave=dict.keys(lista)
    valor=dict.values(lista)
        
    for lista in dic:
        if lista in dic[chave]:
            dic[chave]=valor
    
    return dic