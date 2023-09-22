def total(lista,produtos):
    '''...'''
    dic={}
    
    for produtos in lista:
        if produtos in dic:
            dic[produtos]=dic[produtos]+1
 
    return dic