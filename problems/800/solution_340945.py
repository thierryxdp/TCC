def total(lista,produtos):
    '''...'''
    
    produtos=str.split(lista)
    dic={}
    
    for produto in produtos:
        if produtos not in dic:
            dic=dic[produto]
        else:
            dic=dic[produto]+1
    return dic