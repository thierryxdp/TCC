def total(lista,produtos):
    '''...'''
    dic={}
    
    for produto in lista:
        if produto in dic:
            dic[produto]=dic.get(produto)+1 
 
    return lista