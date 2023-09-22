def total(lista,produtos):
    '''...'''
    dic={}
    
    for produtos in lista:
        if produtos in dic:
            dic=dic+produtos
 
    return dic