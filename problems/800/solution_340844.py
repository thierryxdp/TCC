def total(lista,produtos):
    '''...'''
    
    dic={}
    for produto in produtos:
        if produto in dic:
            dic[produto]=dic[produto]+1
    return dic