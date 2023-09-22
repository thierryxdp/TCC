def total(lista,produtos):
    '''...'''
    dic={}
    
    for produto in lista:
        if produtos in lista[produto]:
            dic[produto]=dic[produto]+1
    return dic