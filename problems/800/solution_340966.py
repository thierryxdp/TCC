def total(lista,produtos):
    '''...'''
    
    produtos=produtos.split()
    dic={}
    
    for produto in produtos:
        if produto not in dic:
            dic=dic[produto]
        else:
            dic=dic[produto]+1
    return dic