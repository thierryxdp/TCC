def total(lista,produtos):
    '''...'''
    
    dic={}
    
    for produto in produtos:
        if produto in dic:
            dic[produtos]=dic.get(produtos)+1
    return dic