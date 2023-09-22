def total(lista,produtos):
    '''...'''
    
    dic={}
    
    for produto in produtos:
        if produto not in dic:
            dic[produtos]=1
        else:
            dic[produtos]=dic.get(produtos)+1        
    return dic