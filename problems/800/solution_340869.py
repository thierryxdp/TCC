def total(lista,produtos):
    '''...'''
    
    dic={}
    for produto in produtos:
        if produto in lista:
            dic[produto]=dic.get[produto]+1
    return lista