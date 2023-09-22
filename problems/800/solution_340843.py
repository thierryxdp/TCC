def total(lista,produtos):
    '''...'''
    
    dic={}
    for produto in produtos:
        if produto in dic:
            dic=dic+produto
    return dic