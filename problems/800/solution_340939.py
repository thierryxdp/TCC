def total(lista,produtos):
    '''...'''
    
    palavras=str.split(lista)
    dic={}
    
    for palavra in palavras:
        if palavra not in dic:
            dic=dic[produto]
        else:
            dic=dic[produto]+1
    return dic