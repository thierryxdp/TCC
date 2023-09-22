def total(lista,produtos):
    '''...'''
    
    palavras=str.split(lista)
    dic={}
    for produto in palavras:
        if produtos in dic:
            dic=dic[produto]+1
    return dic