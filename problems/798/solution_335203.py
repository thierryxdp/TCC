def freq_palavras(frases):
    '''...'''
    
    lista=str.split(frases)
    dic=''
    chave=dict.keys(dic)
    valor=dict.values(dic)
        
    for lista in frases:
        if lista in valor:
            lista=chave+1
    
    return lista