def total(lista,produtos):
    '''...'''
    dic={}
    
    for produto in produtos:
        if produto not in dic:
            dic=dic[produto]
        else:
            dic=dic[produto]+1
    return dic