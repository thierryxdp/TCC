def total(lista,produtos):
    '''...'''
    dic={}
    
    for produtos in lista:
        if produtos in dic:
            dic[produto]=dic.get(produto)+1 
 
    return lista