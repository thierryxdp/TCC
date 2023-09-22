def total(lista,produtos):
    '''...'''
    
    dic={}
    
    for lista in produtos:
        if produtos in dic:
            dic[lista]=dic[lista]+1
    return dic