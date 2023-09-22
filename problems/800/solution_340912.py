def total(lista,produtos):
    '''...'''
    
    palavras=str.split(lista)
    dic={}
    
    for palavra in palavras:
        if palavra in dic:
            dic=dic[produto]+1
    return dic