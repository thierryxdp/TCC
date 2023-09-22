def total(lista,produtos):
    '''...'''
    
    produtos=str.split(lista)
    dic={}
    
    for produto in produtos:
        if produto in dic:
            dic=dic[produto]+1
    return dic