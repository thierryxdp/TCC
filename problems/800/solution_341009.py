def total(lista,produtos):
    '''...'''
    
    produtos=str.split(lista)
    dic={}
    
    for produtos in produto:
        if produto not in dic:
            dic=dic[produto]
        else:
            dic=dic[produto]+1
    return dic