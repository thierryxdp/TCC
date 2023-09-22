def total(lista,produtos):
    '''...'''
    produtos=dict.values(lista)
    dic={}
    
    for produto in produtos:
        if produto not in dic:
            dic[produto]=1
        else:
            dic[produto]=dic.get(produto)+1 

    return lista