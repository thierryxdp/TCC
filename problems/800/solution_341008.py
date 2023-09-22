def total(lista,produtos):
    '''...'''
    
    lista=str.split(lista)
    dic={}
    
    for lista in produto:
        if produto not in dic:
            dic=dic[produto]
        else:
            dic=dic[produto]+1
    return dic