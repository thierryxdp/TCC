def total(lista,produtos):
    '''...'''
    dic={}
    
    for produto in produtos:
        if produto not in dic:
            dic[produto]=1
        else:
            dic[produto]=dic.values(lista)+1

    return dic